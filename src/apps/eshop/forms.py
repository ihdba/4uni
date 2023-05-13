from django import forms
from .models import Product, Supplier

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["product_name", "product_description", "supplier", "price","product_image"]


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ["supplier_name", "email"]