from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        field = ['username','first_name','last_name','email','is_active']   
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data).id
        return user
    
    def get_users(self):
        return UserSerializer(User.objects.all(),many= True).data
    
    def remove_users(self,id):
        user=User.objects.filter(id=id).update(is_active=False)
        
    def update_user(self,id,validated_data):
        user= User.objects.filter(id=id).update(**validated_data)
        return user

    
