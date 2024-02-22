# Generated by Django 3.1.7 on 2021-03-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210308_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='chapters',
            field=models.ManyToManyField(to='books.Chapter'),
        ),
    ]