# Generated by Django 4.2.6 on 2023-12-26 11:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ShopApp", "0007_rename_contact_u_contact_us"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact_us",
            old_name="messgae",
            new_name="message",
        ),
    ]
