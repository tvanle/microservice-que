from django.db import models

class Recommendation(models.Model):
    customer_id = models.IntegerField()
    book_ids = models.JSONField(default=list)
    reason = models.CharField(max_length=255, default='Based on ratings and popularity')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for Customer {self.customer_id}"
