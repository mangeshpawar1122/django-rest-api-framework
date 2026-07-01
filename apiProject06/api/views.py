from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book,Author
from .serializers import BookSerializers,AuthorSerializers
# Create your views here.


# Normal Query Without optimization
@api_view(['GET'])
def all_book(request):
  books = Book.objects.all()# N + 1 Query Problem
  serializer = BookSerializers(books,many=True)
  return Response(serializer.data)


# Using select_releted to optimize ForeignKey RelationShips
@api_view(['GET'])
def select_book(request):
  books=Book.objects.select_related('author').all() # Optimized Query
  serializer = BookSerializers(books,many=True)
  return Response(serializer.data)

# using a prefetch_releted to optimize reverse ForeignKey ReletionShips
@api_view(['GET'])
def prefetch_authors(request):
  author = Author.objects.prefetch_related('books').all() # Optimized Query
  serializer = AuthorSerializers(author,many=True)
  return Response(serializer.data)