# Generated by Django 4.0.1 on 2022-01-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_pizza_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzatype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
