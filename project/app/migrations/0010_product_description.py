# Generated by Django 3.0.9 on 2020-08-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='detail of product'),
        ),
    ]
