# Generated by Django 4.2.1 on 2023-05-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_supplier_supplier_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='registered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]