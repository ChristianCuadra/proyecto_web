# Generated by Django 5.0.6 on 2024-07-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(upload_to='productos/'),
        ),
    ]
