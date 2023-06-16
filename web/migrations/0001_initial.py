# Generated by Django 3.2.9 on 2023-02-13 10:04

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_No',
            fields=[
                ('id', models.BigAutoField(default=web.models.generate_8_digit_id, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=400)),
                ('Link', models.URLField()),
                ('service_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.service_no')),
            ],
        ),
    ]
