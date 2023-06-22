# Generated by Django 4.2.2 on 2023-06-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='home_page_description',
            field=models.TextField(default='Description', max_length=20, verbose_name='Home Page Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=8000, verbose_name='Description'),
        ),
    ]