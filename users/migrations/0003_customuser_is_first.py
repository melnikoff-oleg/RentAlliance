# Generated by Django 3.0.4 on 2020-04-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_is_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_first',
            field=models.BooleanField(default=True),
        ),
    ]
