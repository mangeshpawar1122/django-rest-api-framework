from django.urls import path
from .views import StudentList

urlpatterns = [
    path('student/',StudentList.as_view()), # for GET(all)  and POST
    path('student/<int:pk>/',StudentList.as_view()), # for GET(single),PUT,DELETE
]
