# Generated by Django 2.2.16 on 2020-11-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201104_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_post',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Título'),
        ),
    ]
