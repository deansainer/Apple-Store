# Generated by Django 4.2.1 on 2023-05-27 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories'},
        ),
    ]
