from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    middle_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Middle Name"
    )
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name", "-is_active"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Price (CHF)"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="Category",
    )
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name="books", verbose_name="Author"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-published_date"]
        indexes = [models.Index(fields=["title", "price", "published_date", "author"])]

    def __str__(self):
        return self.title

    def is_available(self):
        return self.stock > 0
