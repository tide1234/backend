from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password
class userSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):

        if data['first_name'] == "tide":
            raise ValueError ("error")
        else:
            return data
        

    def create (self,data):
        pwd = data['password']
        encrypted_pwd = make_password(pwd,"2jhgehdjsUJ@£567^djhwkdm234")
        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data ['last_name'],
            email = data['email'],
            photo = data['photo'],
            username = data['username'],
            password = encrypted_pwd

        )
       # user['password'] = encrypted_pwd


        return user
class LoginSerializer(serializers.Serializer):
    email  = serializers.CharField()
    password = serializers.CharField()

    def loginuser(self,data):
        user = User.objects.filter(email = data['email']).first()
        if user is not None:
            original_pwd = data['password']

            encrypted_pwd = getattr(user, "password")

            check = check_password(original_pwd, encrypted_pwd)   
            
            if check == True:
                user={
                    "first_name": getattr(user, "first_name"),
                    "last_name": getattr(user, "last_name"),
                    "email": getattr(user, "email"),
                    "id": getattr(user, "id")

                }
                return user
            
        
            else:
                raise ValueError ("Invalid Credentials")
        else:
            raise ValueError("Invalid credentials")

        