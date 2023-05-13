from django.db import models

from apps.suppliers.models import Supplier



# class Supplier(models.Model):

#     supplier_name = models.CharField("supplier's name", max_length=100, default='deli')
#     email = models.EmailField()


#     def __str__(self):
#         return self.supplier_name

#     class Meta:
#         ordering = ["supplier_name"]
#         verbose_name_plural = "Suppliers"



# Product Class

class Product(models.Model):
    product_name = models.CharField("product's name", max_length=100)
    product_description = models.CharField(max_length=250)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='images/eshop/', blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.product_name

    class Meta:
            ordering = ["product_name"]
            verbose_name_plural = "Products"




# Add to Product Foreign Key of Partner