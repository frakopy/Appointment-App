# Generated by Django 5.0.6 on 2024-06-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "appointment",
            "0007_alter_appointment_barber_alter_appointment_comments_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="comments",
            field=models.TextField(blank=True, null=True),
        ),
    ]
