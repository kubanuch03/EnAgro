# Generated by Django 4.2.8 on 2024-01-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_like", "0002_alter_like_register_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="register_date",
            field=models.DateTimeField(),
        ),
    ]