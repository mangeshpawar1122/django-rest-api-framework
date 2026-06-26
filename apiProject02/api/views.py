from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers 
# Create your views here.

@api_view(['GET'])
def get_student(request):
  students = Student.objects.all()
  serializers = StudentSerializers(students,many=True)
  return Response(serializers.data)