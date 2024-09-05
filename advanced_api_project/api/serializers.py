from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields

    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future.
        """
        import datetime
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and nested books
