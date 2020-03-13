# Generated by Django 2.2.5 on 2020-01-25 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to=settings.AUTH_USER_MODEL),
        ),
    ]
