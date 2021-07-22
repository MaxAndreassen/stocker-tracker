import uuid
from django.db import models

class Stock(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    created_at = models.DateTimeField('date_created');
    updated_at = models.DateTimeField('date_updated');
    deleted_at = models.DateTimeField('date_deleted');
    name = models.CharField(max_length=20);
    ticker = models.CharField(max_length=5);

class OrderType(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    created_at = models.DateTimeField('date_created');
    updated_at = models.DateTimeField('date_updated');
    deleted_at = models.DateTimeField('date_deleted');
    name: models.CharField(max_length=20);
    description: models.CharField(max_length=50);

class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    created_at = models.DateTimeField('date_created');
    updated_at = models.DateTimeField('date_updated');
    deleted_at = models.DateTimeField('date_deleted');
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE);
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE);

    