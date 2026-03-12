from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BookCatalog(models.Model):
    book_id = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)

    class Meta:
        unique_together = ('book_id', 'category')

    def __str__(self):
        return f"Book {self.book_id} in {self.category.name}"
