# Generated by Django 5.0 on 2023-12-31 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0003_alter_cafeteria_maps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodjournalimage',
            name='journal_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffee_images', to='cafeteria.foodjournalentry'),
        ),
    ]
