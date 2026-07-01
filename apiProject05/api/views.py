from django.shortcuts import render
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
  if request.method == 'GET':
    return Response({'message':"Public can view this Data and List of Posts"})
  elif request.method == 'POST':
    return Response({'message':f"Data created by {request.user.username}"})
