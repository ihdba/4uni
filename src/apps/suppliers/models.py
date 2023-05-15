from django.db import models

# Create your models here.



class Supplier(models.Model):

    supplier_name = models.CharField("supplier's name", max_length=100, default='deli')
    supplier_info = models.TextField(blank=True)
    email = models.EmailField()
    registered = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.supplier_name

    class Meta:
        ordering = ["supplier_name"]
        verbose_name_plural = "Suppliers"





