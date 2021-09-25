
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cerberus import Validator

from ..serializers import UserSerializer

class UserApi(APIView):
    def post(self,request):
        validator= Validator({
            'username': {'required':True,'type':'integer'},
            'first_name':{'required':True.'type':'string'},
            'last_name':{'required':True,'type':'string'},
            'email':{'required':True,'type':'string'},
        })

    if not Validator.validate(request.data):
        return Response({
            'errors':validator.errors
        }status=status.HTTP_400_BAD_REQUEST)
    
    serializer= UserSerializer()
    serializer.create(request.data)

    return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        serializer = UserSerializer()
        users =serializer.get_users()

        return Response(
            {
                'data':users
            }, status=status.HTTP_200_OK)

    def delete(self, request):
        if not request.GET.get('username'):
            return Response({
                'errors':'Usuario invalido',
            },status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer()
        serializer.remove_users(request.GET['username'])
        return Response('Confirmdo':'Estudiante eliminado',status=status.HTTP_200_OK)


    def post(self,request):
        validator= Validator({
            'username': {'required':True,'type':'integer'},
            'first_name':{'required':True.'type':'string'},
            'last_name':{'required':True,'type':'string'},
            'email':{'required':True,'type':'string'},
        })

    if not Validator.validate(request.data):
        return Response({
            'errors':validator.errors
        }status=status.HTTP_400_BAD_REQUEST)
  
        if not request.GET.get('username'):
            return Response({
                'errors':'Usuario invalido',
            },status=status.HTTP_400_BAD_REQUEST)
    serializer= UserSerializer()
    print(request.GET['id'])
    print(type(request.GET['id']))
    serializer.update_user(request.GET['id'].request.data)

    return Response(status=status.HTTP_202_ACCEPTED)

