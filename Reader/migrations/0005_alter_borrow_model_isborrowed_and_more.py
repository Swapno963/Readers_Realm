# Generated by Django 4.2.7 on 2024-01-03 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0004_remove_reader_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_model',
            name='IsBorrowed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='borrow_model',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Reader.reader'),
        ),
    ]