# Generated by Django 4.1.4 on 2022-12-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_faculty"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="title",
            field=models.CharField(default="sets", max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="school",
            name="title",
            field=models.CharField(default="cse", max_length=10),
            preserve_default=False,
        ),
    ]
