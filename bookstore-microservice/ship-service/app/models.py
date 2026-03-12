import uuid
from django.db import models

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('preparing', 'Preparing'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
    ]
    order_id = models.IntegerField(unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing')
    estimated_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipment for Order #{self.order_id} - {self.status}"
