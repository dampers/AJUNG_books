# Generated by Django 2.2.5 on 2020-01-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_number',
            field=models.IntegerField(default=0),
        ),
    ]
