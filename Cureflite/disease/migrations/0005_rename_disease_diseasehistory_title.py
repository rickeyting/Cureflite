# Generated by Django 4.2.1 on 2023-05-17 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_badhabitsgroup_chinese_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasehistory',
            old_name='disease',
            new_name='title',
        ),
    ]