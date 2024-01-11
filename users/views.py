from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import RegisterUserSerializer, LoginUserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')

        # Check if a user with the provided username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return Response({
                'status': 'failed',
                'message': 'User with this username or email already exists.'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)

        return Response({
            'status': 'success',
            'message': 'User created!'
        }, status=status.HTTP_201_CREATED)
    
class LoginView(generics.CreateAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'status': 'success',
                'message': 'Logged-in successfuly!',
                'token': token.key
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

