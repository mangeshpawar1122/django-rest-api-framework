from rest_framework import serializers
from .models import Book,Author

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class AuthorSerializers(serializers.ModelSerializer):
  books = BookSerializers(many=True,read_only=True)
  class Meta:
    model = Author
    fields = ['id','name','books']