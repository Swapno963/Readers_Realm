# Generated by Django 4.2.7 on 2024-01-02 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0001_initial'),
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_borrower', to='Reader.reader'),
        ),
    ]
