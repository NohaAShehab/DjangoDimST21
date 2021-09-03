# Generated by Django 3.2.6 on 2021-08-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_departments'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='f', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='masters',
            field=models.BooleanField(null=True),
        ),
    ]