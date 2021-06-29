# Generated by Django 3.1.4 on 2021-01-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['firstname', 'lastname'], 'verbose_name': 'autor', 'verbose_name_plural': 'autorzy'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'książka', 'verbose_name_plural': 'książki'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name'], 'verbose_name': 'wydawca', 'verbose_name_plural': 'wydawcy'},
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
