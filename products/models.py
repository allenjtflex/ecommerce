from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False )
    discription = models.TextField(max_length=4000, null=True, blank=True)
    price    = models.DecimalField(decimal_places=2,max_digits=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
