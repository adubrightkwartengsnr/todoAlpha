# Generated by Django 3.2.9 on 2023-07-19 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
