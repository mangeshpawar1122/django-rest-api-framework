from django.urls import path
from . import views
urlpatterns = [
    path('books/',views.all_book,name='all_book'),
    path('books/select/',views.select_book,name='select_book'),
    path('authors/prefetch/',views.prefetch_authors,name='prefetch_authors'),

]
