# Generated by Django 4.2.6 on 2023-10-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='mail',
            field=models.CharField(max_length=100, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name_car',
            field=models.CharField(max_length=100, verbose_name='Название машины'),
        ),
        migrations.AlterField(
            model_name='task',
            name='phone_num',
            field=models.CharField(max_length=100, verbose_name='Номер телефона'),
        ),
    ]
