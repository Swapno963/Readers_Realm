# Generated by Django 4.2.7 on 2024-02-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0007_alter_borrow_model_isborrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reader_images/'),
        ),
    ]
