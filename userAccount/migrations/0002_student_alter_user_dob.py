# Generated by Django 4.0.6 on 2022-07-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('classs', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(verbose_name='DOB'),
        ),
    ]
