# Generated by Django 3.1.4 on 2021-01-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210127_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
