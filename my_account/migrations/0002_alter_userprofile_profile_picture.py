# Generated by Django 4.2.3 on 2023-12-01 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='images/userprofile'),
        ),
    ]
