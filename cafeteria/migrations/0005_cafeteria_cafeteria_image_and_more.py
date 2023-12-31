# Generated by Django 4.2.3 on 2024-01-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0004_alter_foodjournalimage_journal_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafeteria',
            name='cafeteria_image',
            field=models.ImageField(blank=True, null=True, upload_to='cafeterias'),
        ),
        migrations.AlterField(
            model_name='foodjournalentry',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
