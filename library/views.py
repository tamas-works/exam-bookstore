from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend # pyright: ignore[reportMissingModuleSource]
from .models import  Author, Book, Category
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer


# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["first_name", "middle_name", "last_name"]
    ordering_fields = ["first_name", "last_name", "created_at"]
    ordering = ["last_name", "first_name"]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["is_active"]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "is_active", "created_at"]
    ordering = ["name"]
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author","category").all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["author", "published_date",]
    search_fields = ["title", "author__first_name", "author__last_name", "category__name"]
    ordering_fields = ["title", "published_date", "price", "stock"]
    ordering = ["title", "-published_date"]

    @action(detail=False, methods=["get"])
    def available(self, request):
        available_books = self.queryset.filter(stock__gt=0)

        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"])
    def low_stock(self, request):
        low_stock_books = self.queryset.filter(stock__lte=5, stock__gt=0)

        serializer = self.get_serializer(low_stock_books, many=True)
        return Response(serializer.data)
    