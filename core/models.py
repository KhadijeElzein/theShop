from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products',blank=True)

    def __str__(self):
        return self.name