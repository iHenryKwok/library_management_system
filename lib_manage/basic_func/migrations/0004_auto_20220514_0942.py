# Generated by Django 3.2 on 2022-05-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_func', '0003_alter_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=32, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=64, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='press',
            field=models.CharField(max_length=32, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='card',
            name='institution',
            field=models.CharField(max_length=32, verbose_name='机构'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]