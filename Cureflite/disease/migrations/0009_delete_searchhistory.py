# Generated by Django 4.2.1 on 2023-05-20 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0008_remove_bodyparts_symptom_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SearchHistory',
        ),
    ]
