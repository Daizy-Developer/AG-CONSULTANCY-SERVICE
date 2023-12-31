# Generated by Django 3.2.9 on 2023-02-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20230213_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=150)),
                ('Phone', models.CharField(max_length=25)),
                ('Looking', models.CharField(max_length=50)),
                ('Status', models.BooleanField(default=False)),
                ('Budget', models.IntegerField()),
            ],
        ),
    ]
