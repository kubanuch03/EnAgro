# Generated by Django 4.2.8 on 2024-02-11 17:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_users", "0004_alter_customuser_client_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="client_rating",
        ),
    ]
