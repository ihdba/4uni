from django.db import models

# Create your models here.



class Product(models.Model):
    product_name = models.CharField("product's name", max_length=100)
    product_description = models.CharField(max_length=250)
    price = models.FloatField()
    product_image = models.ImageField(upload_to='images/eshop/', blank=True)


    def __str__(self):
        return self.product_name

    class Meta:
            ordering = ["product_name"]
            verbose_name_plural = "Products"