# Generated by Django 3.2.7 on 2021-09-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210926_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
