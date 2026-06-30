# from django.shortcuts import render
# from rest_framework .views import APIView
# from rest_framework. response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializers
# # Create your views here.

from rest_framework import mixins,generics
from .models import Student
from .serializers import StudentSerializers
# CRUD operation using GenericAPIView and Mixins
class StudentListCreateApi(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  generics.GenericAPIView,
):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers
  # read all data
  def get(self,request,*args, **kwargs):
    return self.list(request,*args, **kwargs)
  # create a post Api
  def post(self,request,*args, **kwargs):
    return self.create(request,*args, **kwargs)

class StudentRetrieveUpdateDeleteApi(
  generics.GenericAPIView,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.RetrieveModelMixin
):
  queryset = Student.objects.all()
  serializer_class = StudentSerializers
  lookup_field = 'pk'

  # single data get
  def get(self,request,*args, **kwargs):
    return self.retrieve(request,*args, **kwargs)
  
  # update data using put api
  def put(self,request,*args, **kwargs):
    return self.update(request, *args, **kwargs)
  
  # delete data usign delete
  def delete(self,request,*args, **kwargs):
    return self.destroy(request,*args, **kwargs)

  

# # CRUD operation using APIViews
# class StudentList(APIView):
#   # Read all or single data
#   def get(self, request, pk=None):
#     if pk:
#       try:
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializers(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#       except Student.DoesNotExist:
#         return Response({"error":'Student Not Found'},status=status.HTTP_404_NOT_FOUND)
#     else:
#       # Read all data 
#       students = Student.objects.all()
#       serializer = StudentSerializers(students,many=True)
#       return Response(serializer.data, status=status.HTTP_200_OK)
    
# # Create Data ( POST) 
#   def post(self,request):
#     serializer = StudentSerializers(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

# Update Data (PUT)
#   def put(self,request,pk):
#     try:
#       student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:  
#       return Response({'error':"student not found"},status=status.HTTP_404_NOT_FOUND)
    
#     serializer = StudentSerializers(student, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
  
# # DELETE Data(DELETE)
#   def delete(self,request,pk):
#     try:
#       student = Student.objects.get(pk=pk)
#       student.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)
#     except Student.DoesNotExist:
#       return Response({'error':"student not found"},status=status.HTTP_404_NOT_FOUND)
