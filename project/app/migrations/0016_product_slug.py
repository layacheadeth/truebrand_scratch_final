# Generated by Django 3.0.9 on 2020-08-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200812_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
