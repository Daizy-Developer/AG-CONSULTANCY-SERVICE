# Generated by Django 3.2.9 on 2023-02-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_quotation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('Link', models.URLField()),
            ],
        ),
    ]
