# Generated by Django 4.2.2 on 2024-01-08 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_blogmodel_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='title',
        ),
    ]
