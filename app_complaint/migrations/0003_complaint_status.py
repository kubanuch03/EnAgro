# Generated by Django 4.2.8 on 2023-12-22 03:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_complaint", "0002_alter_complaint_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaint",
            name="status",
            field=models.CharField(
                choices=[
                    ("Запрещенный товар", "Тип жалобы 1"),
                    ("Спам", "Тип жалобы 2"),
                    ("Дубликат", "Тип жалобы 3"),
                    ("Неверная категория", "Тип жалобы 4"),
                    ("Мошенничество", "Тип жалобы 5"),
                    ("Другая причина", "Тип жалобы 6"),
                ],
                default="Спам",
                max_length=20,
            ),
        ),
    ]
