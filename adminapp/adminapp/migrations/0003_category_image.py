# Generated by Django 4.1.7 on 2023-03-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
