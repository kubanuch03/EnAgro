# Generated by Django 4.2.8 on 2023-12-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_users", "0003_alter_customuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="avatar/%Y/%m/%d/"
            ),
        ),
    ]