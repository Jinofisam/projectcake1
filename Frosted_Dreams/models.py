from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )


class cakeorder(models.Model):
      quantity = models.PositiveBigIntegerField()
      customization = models.TextField(blank=True)
      delivery_date = models.DateField()
      cake_name = models.CharField(max_length=255,default='Cake')  
      price = models.DecimalField(max_digits=10, decimal_places=2, default=1200)
class Meta:
      db_table = "orders"


