# Generated by Django 3.1.7 on 2021-03-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitemap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='no-url', max_length=200, verbose_name='chapter link')),
                ('text', models.TextField(default='empty', verbose_name='chapter text')),
            ],
        ),
    ]