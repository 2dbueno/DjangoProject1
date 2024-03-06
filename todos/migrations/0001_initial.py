# Generated by Django 5.0.2 on 2024-03-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=100, verbose_name="Título")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateField(verbose_name="Data de entrega")),
                ("finished_at", models.DateField(null=True)),
            ],
            options={
                "ordering": ["deadline"],
            },
        ),
        migrations.CreateModel(
            name="Users",
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
                ("nome_usuario", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("senha", models.CharField(max_length=100)),
            ],
        ),
    ]
