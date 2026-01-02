from django.contrib import admin
from .models import Author, Book, Category

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name", "created_at", "updated_at")
    search_fields = ("first_name", "middle_name", "last_name")
    list_filter = ("first_name", "last_name")
    readonly_fields = ("created_at", "updated_at")
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at",)
    search_fields = ("name"," description")
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "published_date", "price", "stock","created_at", "updated_at")
    search_fields = ("title", "author__first_name", "author__last_name", "category__name")
    list_filter = ("category", "author", "published_date")
    readonly_fields = ("created_at", "updated_at")