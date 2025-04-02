from rest_framework import serializers
from database.models import CustomUser, IndividualMember, CorporateMember, Director

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Can be written but NOT returned in responses
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        # username and email validation message will be rendered from the model
        if len(data['password']) < 8:
            raise serializers.ValidationError({'error': 'length of password must be at least 8 characters!'})
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'error': 'password do not match!'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        print(validated_data)
        return super().create(validated_data)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if not data['username']:
            raise serializers.ValidationError({'error': 'username field is required!'})
        if not data['password']:
            raise serializers.ValidationError({'error': 'password field is required!'})
        return super().validate(data)
    
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'gender', 'nationality', 'title', 'position_in_chambers']

class IndividualReadonlySerializer(serializers.ModelSerializer):
    sponsor = serializers.PrimaryKeyRelatedField(queryset = Director.objects.all())
    class Meta:
        model = IndividualMember
        fields = ['id', 'first_name', 'last_name', 'gender', 'profession', 'sponsor']

class IndividualModifySerializer(serializers.ModelSerializer):
    sponsor = serializers.PrimaryKeyRelatedField(queryset = Director.objects.all())
    class Meta:
        model = IndividualMember
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'phonenumber', 'gender', 'nationality', 'title', 'profession', 'sponsor']
   
class CorporateReadonlySerializer(serializers.ModelSerializer):
    sponsor = serializers.PrimaryKeyRelatedField(queryset = Director.objects.all())
    class Meta:
        model = CorporateMember
        fields = ['id', 'first_name', 'last_name', 'gender', 'company_name', 'position_in_company', 'sponsor']
    
class CorporateModifySerializer(serializers.ModelSerializer):
    reg_no = serializers.CharField(required=False)
    sponsor = serializers.PrimaryKeyRelatedField(queryset = Director.objects.all())
    class Meta:
        model = CorporateMember
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'phonenumber', 'gender', 'nationality', 'title', 'company_name', 'core_line_of_business', 'company_interest_in_hungary', 'company_location', 'position_in_company', 'date_of_establishment', 'reg_no', 'sponsor']
