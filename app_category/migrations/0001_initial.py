# Generated by Django 4.2.8 on 2024-01-06 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("img", models.ImageField(blank=True, upload_to="products/%Y/%m/%d")),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="PodCategory",
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
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "img",
                    models.ImageField(blank=True, upload_to="Podcategory/%Y/%m/%d"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="PodCategory",
                        to="app_category.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "podcategory",
                "verbose_name_plural": "podcategory",
                "ordering": ["name"],
            },
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(fields=["name"], name="app_categor_name_92fa29_idx"),
        ),
        migrations.AddIndex(
            model_name="podcategory",
            index=models.Index(fields=["name"], name="app_categor_name_eae140_idx"),
        ),
    ]
