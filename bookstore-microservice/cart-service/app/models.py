from django.db import models

class Cart(models.Model):
    customer_id = models.IntegerField()

    def __str__(self):
        return f"Cart of customer {self.customer_id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Book {self.book_id} x {self.quantity}"
