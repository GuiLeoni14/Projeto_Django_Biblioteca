# Generated by Django 3.2.5 on 2021-07-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="livro",
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
                ("nome", models.CharField(max_length=100)),
                ("autor", models.CharField(max_length=100)),
                ("data", models.CharField(max_length=100)),
                ("quantidade", models.IntegerField(max_length=100)),
                ("editora", models.CharField(max_length=100)),
                ("tipo", models.CharField(max_length=100)),
                ("localizacao", models.CharField(max_length=100)),
            ],
        ),
    ]
