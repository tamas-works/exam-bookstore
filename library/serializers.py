from rest_framework import serializers
from models import Book, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","first_name","middle_name","last_name", "created_at","updated_at",]
        read_only_fields = ["id", "created_at", "updated_at"]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharFieldeld(source="category.name", read_only=True)
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_middle_name = serializers.CharField(
        source="author.middle_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    is_available = serializers.BooleanField(read_only=True)

    class Meta:
        model = Book
        fields = ["id","title","published_date","price","stock","category","author","category_name","is_available","created_at","updated_at",]
        read_only_fields = ["id", "created_at", "updated_at"]