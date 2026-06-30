from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.


# Public view accessible without Authentication
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
  return Response({'message':"This is a Public View accessible to everyone...!"})

# Private View accessible only to Authentication User
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
  return Response({'message':f'Hello {request.user.username} this is private view accessible only to authentication user'})