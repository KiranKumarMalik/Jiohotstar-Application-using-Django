# Generated by Django 5.1.7 on 2025-03-10 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BannerCards',
            new_name='BannerCard',
        ),
        migrations.RenameModel(
            old_name='Cards',
            new_name='Card',
        ),
    ]
