from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers 
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def get_student(request):
  students = Student.objects.all()
  serializers = StudentSerializers(students,many=True)
  return Response(serializers.data)


@api_view(['POST'])
def create_student(request):
  serializers = StudentSerializers(data=request.data)
  if serializers.is_valid():
    serializers.save()
    return Response(serializers.data,status=status.HTTP_201_CREATED)
  return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)