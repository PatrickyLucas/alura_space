# Generated by Django 4.1.5 on 2023-01-19 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0006_fotografia_usurario"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fotografia",
            old_name="usurario",
            new_name="usuario",
        ),
    ]
