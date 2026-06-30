from django.urls import path
from .views import StudentListCreateApi,StudentRetrieveUpdateDeleteApi

urlpatterns = [
    path('student/',StudentListCreateApi.as_view()), #for data  get all  post
    path('student/<int:pk>/',StudentRetrieveUpdateDeleteApi.as_view()), # for get data put and delete 
]

# from .views import StudentList,

# urlpatterns = [
#     path('student/',StudentList.as_view()), # for GET(all)  and POST
#     path('student/<int:pk>/',StudentList.as_view()), # for GET(single),PUT,DELETE
# ]
