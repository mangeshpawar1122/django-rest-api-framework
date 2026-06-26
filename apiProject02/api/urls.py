from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.get_student,name='get-student'),
    path('add/student/',views.create_student,name='create_student'),
    path('student/update/<int:pk>/',views.update_student,name='update-student'),
    path('student/delete/<int:pk>/',views.delete_student,name='delete_student'),
]