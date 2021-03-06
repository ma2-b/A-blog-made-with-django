# Generated by Django 4.0.4 on 2022-05-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='webiste_url',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
