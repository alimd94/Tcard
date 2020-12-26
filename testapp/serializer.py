from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
# from django.conf import settings
from .models import User,Product
# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from django.core import exceptions
# Register serializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], 
        password = validated_data['password'], 
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'])
        return user
    
    def validate(self, data):
         # here data has all the fields which have validated values
         # so we can create a User instance out of it
         user = User(**data)

         # get the password from the data
         password = data.get('password')

         errors = dict() 
         try:
             # validate the password and catch the exception
             validators.validate_password(password=password, user=User)

         # the exception raised here is different than serializers.ValidationError
         except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)

         if errors:
             raise serializers.ValidationError(errors)

         return super(RegisterSerializer, self).validate(data)
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'