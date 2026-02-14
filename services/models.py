from django.db import models

class ServicePackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_crypto = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_days = models.IntegerField()
    contact_link = models.URLField()

    def __str__(self):
        return self.name
