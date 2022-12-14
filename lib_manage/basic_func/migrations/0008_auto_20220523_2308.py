# Generated by Django 3.2 on 2022-05-23 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_func', '0007_alter_record_appointed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='admin_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic_func.admin', verbose_name='管理员id'),
        ),
        migrations.AlterField(
            model_name='record',
            name='card_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basic_func.card', verbose_name='借书证id'),
        ),
    ]
