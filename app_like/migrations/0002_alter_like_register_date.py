# Generated by Django 4.2.8 on 2024-01-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_like", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="register_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]