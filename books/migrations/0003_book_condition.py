# Generated by Django 2.2.5 on 2020-01-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='B', max_length=2),
        ),
    ]