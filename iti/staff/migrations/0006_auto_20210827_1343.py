# Generated by Django 3.2.6 on 2021-08-27 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20210825_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='dept',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='staff.departments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
