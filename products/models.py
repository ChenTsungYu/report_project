from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    short_code = models.CharField(max_length=20)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name