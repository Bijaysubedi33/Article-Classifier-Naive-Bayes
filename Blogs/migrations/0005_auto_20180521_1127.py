# Generated by Django 2.0.4 on 2018-05-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_auto_20180521_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='mypics/%Y/%m/%d'),
        ),
    ]