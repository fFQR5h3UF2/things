# Generated by Django 3.1.6 on 2021-03-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Books',
        ),
        migrations.RenameModel(
            old_name='Chapter',
            new_name='Chapters',
        ),
    ]