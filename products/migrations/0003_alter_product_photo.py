# Generated by Django 3.2.25 on 2024-07-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="logos", verbose_name="foto"
            ),
        ),
    ]
