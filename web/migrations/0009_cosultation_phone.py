# Generated by Django 3.2.9 on 2023-03-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_cosultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosultation',
            name='Phone',
            field=models.CharField(default=123, max_length=150),
            preserve_default=False,
        ),
    ]