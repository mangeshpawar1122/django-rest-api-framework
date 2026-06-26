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


@api_view(['PUT','PATCH'])
def update_student(request,pk):
  try:
    student = Student.objects.get(id=pk)
  except Student.DoesNotExist:
    return Response({"error":"student not fount"},status=status.HTTP_404_NOT_FOUND)
  
  # partial update support
  if request.method == 'PATCH':
    serializers = StudentSerializers(student,data=request.data,partial= True)
  else:
    serializers = StudentSerializers(student,data = request.data)
  if serializers.is_valid():
    serializers.save()
    return Response(serializers.data,status=status.HTTP_200_OK)
  return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request,pk):
  try:
    student = Student.objects.get(id=pk)
  except Student.DoesNotExist:
    return Response({"error":"student not fount"},status=status.HTTP_404_NOT_FOUND)
  
  student.delete()
  return Response({"message":"student deleted successfully"},status=status.HTTP_204_NO_CONTENT)