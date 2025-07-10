from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50, unique=True)
    company = models.CharField(max_length=100)
    carbon_footprint = models.FloatField(help_text="in grams of CO₂ per item")
    packaging_type = models.CharField(max_length=100)
    eco_rating = models.IntegerField(help_text="1 to 5 stars")
    category = models.CharField(max_length=100,default="general")

    def __str__(self):
        return f"{self.name} ({self.company})"
