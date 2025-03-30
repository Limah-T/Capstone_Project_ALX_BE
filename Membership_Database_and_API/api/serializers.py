from rest_framework import serializers
from database.models import CustomUser, IndividualMember, CooperateMember

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

# class IndividualMemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IndividualMember
#         exclude = ['profile_photo']

    