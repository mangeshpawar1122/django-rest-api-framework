# from django.shortcuts import render
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated,AllowAny

# # Create your views here.


# # Public view accessible without Authentication
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public_view(request):
#   return Response({'message':"This is a Public View accessible to everyone...!"})

# # Private View accessible only to Authentication User
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def private_view(request):
#   return Response({'message':f'Hello {request.user.username} this is private view accessible only to authentication user'})


# from rest_framework .decorators import api_view
# from rest_framework.response import Response
# from .models import Blog
# from .serializers import BlogSerializers
# from rest_framework import status
# @api_view(['GET','POST'])
# def blog_list(request):
#   if request.method == 'GET':
#     blogs = Blog.objects.all()
#     serializer = BlogSerializers(blogs,many = True)
#     return Response(serializer.data)
#   elif request.method == 'POST':
#     serializer = BlogSerializers(data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#   return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# API only for authenticated users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
  user = request.user
  return Response({
    "username":user.username,
    "email":user.email,
    "is_staff":user.is_staff,
  })


# API Only for admin user
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
  return Response({'message':f"WelCome to the Admin panel, {request.user.username}... !"})