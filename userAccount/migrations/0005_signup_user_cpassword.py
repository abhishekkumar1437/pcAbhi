# Generated by Django 4.0.6 on 2022-08-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0004_remove_signup_user_cpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_user',
            name='cpassword',
            field=models.TextField(default=0),
        ),
    ]
