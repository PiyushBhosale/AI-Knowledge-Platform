from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id','username','email', 'date_joined']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = user
        fields = ['username','email','password']

    def create(self, validated_data):
        User = user.objects.create_user(
        username = validated_data['username'],
        email = validated_data['email'],
        password = validated_data['password']
        )
        return User
    
    def validate_username(self,value):
        if len(value) < 3:
            raise serializers.ValidationError("Username must be more than 3 chars")
    
    def validate(self, data):
        if data['username'] == data['password']:
            raise serializers.ValidationError("Username and password can't be same")
        return data