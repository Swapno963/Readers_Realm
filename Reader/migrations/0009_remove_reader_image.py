# Generated by Django 4.2.7 on 2024-02-28 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0008_reader_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='image',
        ),
    ]