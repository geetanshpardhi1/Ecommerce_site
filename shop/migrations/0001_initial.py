# Generated by Django 4.2 on 2023-06-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
                ('product_desc', models.TextField()),
                ('discount_price', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
