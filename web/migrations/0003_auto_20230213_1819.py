# Generated by Django 3.2.9 on 2023-02-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_service_no_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='Description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]