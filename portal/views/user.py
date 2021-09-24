
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
            'errors':validator.errorsm
        }status=status.HTTP_400_BAD_REQUEST)
    
    serializer= UserSerializer()
    serializer.create(request.data)

    return Response(status=status.)

BRB