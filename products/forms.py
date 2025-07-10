# products/forms.py

from django.core.exceptions import ValidationError
from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'company', 'barcode',
            'carbon_footprint', 'packaging_type',
            'eco_rating', 'category'
        ]
        widgets = {
            'eco_rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_barcode(self):
        barcode = self.cleaned_data.get('barcode')
        if Product.objects.filter(barcode=barcode).exists():
            raise ValidationError("🚫 A product with this barcode already exists.")
        return barcode
