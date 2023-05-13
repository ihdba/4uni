from django.db import models

# Create your models here.



class Supplier(models.Model):

    supplier_name = models.CharField("supplier's name", max_length=100, default='deli')
    email = models.EmailField()


    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ["supplier_name"]
        verbose_name_plural = "Suppliers"
