# Generated by Django 2.1.7 on 2019-02-23 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelmessage',
            name='dispatch_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='modelmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='modelroom',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='modelroom',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='modelroom',
            name='participants',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL, verbose_name='Участники'),
        ),
    ]