# Generated by Django 5.1.1 on 2024-10-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0002_alter_payment_pay_type_alter_payment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="pay_type",
            field=models.CharField(
                choices=[("payment", "Payment"), ("fine", "Fine")],
                default="payment",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("paid", "Paid"),
                    ("expired", "Expired"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
    ]