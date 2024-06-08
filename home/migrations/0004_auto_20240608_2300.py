# Generated by Django 3.0.5 on 2024-06-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_student_address_remove_student_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
