from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.get_student,name='get-student'),
    path('add/student/',views.create_student,name='create_student'),
]