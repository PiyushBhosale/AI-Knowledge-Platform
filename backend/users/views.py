from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListView(APIView):
    def get(self,request):
        users = User.objects.all().values('id','username','email','password')
        return Response(list(users))