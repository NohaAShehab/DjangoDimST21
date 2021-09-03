# Generated by Django 3.2.6 on 2021-08-25 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_staff_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]