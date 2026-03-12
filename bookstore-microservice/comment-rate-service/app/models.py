from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Comment(models.Model):
    customer_id = models.IntegerField()
    book_id = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by Customer {self.customer_id} on Book {self.book_id}"

class Rating(models.Model):
    customer_id = models.IntegerField()
    book_id = models.IntegerField()
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('customer_id', 'book_id')

    def __str__(self):
        return f"Rating {self.score}/5 by Customer {self.customer_id} on Book {self.book_id}"
