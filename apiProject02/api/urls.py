from django.urls import path
from . import views

urlpatterns = [
    path('get-student/',views.get_student,name='get-student'),
]