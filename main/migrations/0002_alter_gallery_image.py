# Generated by Django 4.0.4 on 2022-05-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='main/static/img/gallery'),
        ),
    ]
