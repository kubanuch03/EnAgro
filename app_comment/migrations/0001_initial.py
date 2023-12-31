# Generated by Django 4.2.8 on 2024-01-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_sub", models.BooleanField(default=False)),
                ("body", models.TextField()),
                ("register_date", models.DateTimeField()),
                ("is_confirm", models.BooleanField(default=False)),
            ],
        ),
    ]
