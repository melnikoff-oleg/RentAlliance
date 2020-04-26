# Generated by Django 3.0.4 on 2020-04-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200421_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pk', models.IntegerField(default=0)),
                ('landlord_pk', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
                ('review', models.TextField(default=None, max_length=5000)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='questionnaires',
        ),
        migrations.DeleteModel(
            name='Questionnaire',
        ),
        migrations.AddField(
            model_name='customuser',
            name='surveys',
            field=models.ManyToManyField(to='users.Survey'),
        ),
    ]