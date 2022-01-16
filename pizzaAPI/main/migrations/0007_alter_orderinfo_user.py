# Generated by Django 4.0.1 on 2022-01-16 10:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_orderinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='user',
            field=models.OneToOneField(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
