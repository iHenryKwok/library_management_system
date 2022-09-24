# Generated by Django 3.2 on 2022-05-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_func', '0002_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.SmallIntegerField(choices=[(1, '古籍'), (2, '文学'), (3, '自然科学'), (4, '哲学、宗教'), (5, '社会科学'), (6, '医药、卫生'), (7, '工业技术'), (8, '环境科学、安全科学'), (9, '综合性图书')], verbose_name='类别'),
        ),
    ]
