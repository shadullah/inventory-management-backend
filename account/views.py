from django.shortcuts import render
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from .serializers import UserSerializer,LoginSerializer, ProfileSerializer
from .models import MyOne

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

# Create your views here.
class RegView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            return Response("User registered successful")
        return Response(serializer.errors)
    
class UsersInfo(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer

class loginVIew(APIView):
    def post(self, request):
        serializer=LoginSerializer(data=request.data)

        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']

            try:
                user= User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'user not found'})
            
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                accessToken=refresh.access_token

                return Response({
                    'user':UserSerializer(user).data,
                    'refresh': str(refresh),
                    'access':str(accessToken)
                }, status=status.HTTP_200_OK)
            
        return Response({'error': 'invalid credentials'})

class logOutview(APIView):
    authentication_classes=[BasicAuthentication, TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, req):
        try:
            logout(req)
            return Response({'success':"logout success"})
        except:
            return Response({'error': 'couldn\'t logout'})
        
class ProfileView(viewsets.ModelViewSet):
    queryset=MyOne.objects.all()
    serializer_class=ProfileSerializer