from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import filters
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RegisterSerializer, LoginSerializer, DirectorSerializer, IndividualReadonlySerializer, CorporateReadonlySerializer, IndividualModifySerializer, CorporateModifySerializer
from database.models import CustomUser, Director, IndividualMember, CorporateMember

class RegisterAPI(generics.GenericAPIView, CreateModelMixin): # CMM for post request
    authentication_classes = [] # set to empty so users can register
    permission_classes = []  # set to empty so users can register
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs): # manually defined the post method
        return self.create(request, *args, **kwargs) # called self.create inside post to tell DRF it's a post request        
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        # make_password will turn the plain password into a harsh for database 
        password = make_password(serializer.validated_data['password'])
        user = CustomUser.objects.create(username=username, email=email, password=password, is_active=False)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token':token.key}, status=status.HTTP_201_CREATED)

class LoginAPI(APIView) :
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # Get the instance by the validated username from customuser model to authenticate
            username = CustomUser.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response(data={'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'invalid credentials'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views to list all the endpoints
@api_view(['GET'])
def api_root(request, format=None):
    data= {
        'directors': reverse('directors', request=request, format=format),
        'individual_members': reverse('individual_members', request=request, format=format),
        'corporate_members': reverse('corporate_members', request=request, format=format),
    }
    return Response(data=data, status=200)
 
# List all the directors
class DirectorsAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Director.objects.all().order_by('first_name')
    serializer_class = DirectorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'gender', 'position_in_chambers']
    search_fields = ['first_name', 'last_name', 'gender', 'position_in_chambers']
    ordering_fields = ['first_name', 'last_name','position_in_chambers']
    
# Get each director with thier id/pk
class DirectorAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'

# Create Individual member
class IndividualMemberCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IndividualMember.objects.all()
    serializer_class = IndividualModifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_user = request.user.id
        serializer.validated_data['creator_id'] = current_user
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

# Get all individual members
class IndividualMembersAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IndividualMember.objects.all()
    serializer_class = IndividualReadonlySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'gender', 'profession', 'sponsor']
    search_fields = ['first_name', 'last_name', 'gender', 'profession', 'sponsor']
    ordering_fields = ['first_name', 'last_name', 'profession', 'sponsor']

# Get each individual member with their id/pk
class IndividualMemberAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IndividualMember.objects.all()
    serializer_class = IndividualReadonlySerializer
    lookup_field = 'pk'

    # get the serializer object instance and retrieve based on who created the member
    def get_serializer_class(self):
        current_user_id = self.request.user.id
        instance = self.get_object()
        if instance.creator_id == current_user_id:
            return IndividualModifySerializer
        else:
            return IndividualReadonlySerializer

# Update Individual member
class IndividualMemberUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IndividualMember.objects.all()
    serializer_class = IndividualModifySerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        member_id = kwargs.get('pk')
        member = get_object_or_404(IndividualMember, id=member_id)
        creator_id = member.creator_id
        current_user_id = request.user.id
        if creator_id != current_user_id:
            return Response(data={'error': 'You do have permission to modify this data!'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

# Delete Individual Member
class IndividualMemberDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IndividualMember.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        current_user = request.user.id
        member_id = kwargs.get('pk')
        member = get_object_or_404(IndividualMember, id=member_id)
        if current_user != member.creator_id:
            return Response({'error': 'You are not permitted to delete this data'}, status=status.HTTP_403_FORBIDDEN)
        member.delete()
        return Response({'success': 'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
       
# Register/Create a corporate member
class CorporateMemberCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CorporateMember.objects.all()
    serializer_class = CorporateModifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_user = request.user.id
        serializer.validated_data['creator_id'] = current_user
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

# Get all corporate members
class CorporateMembersAPIView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CorporateMember.objects.all().order_by('first_name')
    serializer_class = CorporateReadonlySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'sponsor', 'position_in_company']
    search_fields = ['first_name', 'last_name', 'sponsor', 'position_in_company']
    ordering_fields = ['first_name', 'last_name','sponsor', 'position_in_company']

# Get each corporate member with their id/pk
class CorporateMemberAPIView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CorporateMember.objects.all()
    serializer_class = CorporateReadonlySerializer
    lookup_field = 'pk'

    # get the serializer object instance and retrieve based on who created the member
    def get_serializer_class(self):
        current_user_id = self.request.user.id
        instance = self.get_object()
        if instance.creator_id == current_user_id:
            return CorporateModifySerializer
        else:
            return CorporateReadonlySerializer
        
# Update each corporate member with their id/pk
class CorporateMemberUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CorporateMember.objects.all()
    serializer_class = CorporateModifySerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        current_user = request.user.id
        member_id = kwargs.get('pk')
        member = get_object_or_404(CorporateMember, id=member_id)
        if current_user != member.creator_id:
            return Response({'error': 'You are not permitted to update this data!'}, status=status.HTTP_202_ACCEPTED)
        return super().update(request, *args, **kwargs)

# Delete each corporate member by their id/pk    
class CorporateMemberDestroyAPIView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CorporateMember.objects.all()
    serializer_class = CorporateModifySerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        current_user = request.user.id
        member_id = kwargs.get('pk')
        member = get_object_or_404(IndividualMember, id=member_id)
        if current_user != member.creator_id:
            return Response({'error': 'You are not permitted to delete this data'}, status=status.HTTP_403_FORBIDDEN)
        member.delete()
        return Response({'success': 'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
