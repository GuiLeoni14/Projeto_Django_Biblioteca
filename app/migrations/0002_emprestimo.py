# Generated by Django 3.2.5 on 2021-07-19 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="emprestimo",
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
                ("dataem", models.CharField(max_length=100)),
                ("pessoa", models.CharField(max_length=100)),
                ("quantidadeem", models.IntegerField(max_length=100)),
                (
                    "nome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.livro"
                    ),
                ),
            ],
        ),
    ]
