# Generated by Django 5.0.4 on 2024-04-29 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Product',
        ),
    ]