from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Student
    # fields = ['name','age','city']  # to include specific fields
    fields = '__all__' # to include all fields