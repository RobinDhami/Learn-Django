# Generated by Django 5.0.6 on 2024-07-04 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]