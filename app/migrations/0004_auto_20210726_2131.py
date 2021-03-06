# Generated by Django 3.2.5 on 2021-07-27 00:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_emprestimo_dataem'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='criado_emp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='editado_emp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='editado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataem',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='livro',
            name='data',
            field=models.DateField(),
        ),
    ]
