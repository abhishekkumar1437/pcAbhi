# Generated by Django 4.0.6 on 2022-09-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
