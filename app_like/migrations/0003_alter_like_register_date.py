# Generated by Django 4.2.8 on 2024-01-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_like", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="register_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
