# Generated by Django 3.2 on 2022-05-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_func', '0006_alter_record_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='appointed',
            field=models.BooleanField(default=False, verbose_name='已被预约'),
        ),
    ]
