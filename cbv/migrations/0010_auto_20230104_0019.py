# Generated by Django 3.1.14 on 2023-01-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("cbv", "0009_move_unique_constraint")]

    operations = [
        migrations.AlterField(
            model_name="klass",
            name="docstring",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="method",
            name="docstring",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="module",
            name="docstring",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="projectversion",
            name="sortable_version_number",
            field=models.CharField(max_length=200),
        ),
    ]
