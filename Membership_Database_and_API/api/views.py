from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer
from database.models import CustomUser

class RegisterAPI(GenericAPIView, CreateModelMixin): # CMM for post request
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
        print(token)
        return Response(data={'token':token.key}, status=status.HTTP_201_CREATED)

class LoginAPI(APIView) :
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            pass_word = serializer.validated_data['password']
            print(user_name, pass_word)
            user = authenticate(request, username=user_name, password=pass_word)
            if user and user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response(data={'token': token}, status=status.HTTP_200_OK)
            return Response({'error': 'invalid credentials'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)