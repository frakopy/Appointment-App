# Generated by Django 5.0.6 on 2024-06-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0009_appointment_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="status",
            field=models.CharField(default="confirmed", max_length=150),
        ),
    ]
