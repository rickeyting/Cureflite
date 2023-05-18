# Generated by Django 4.2.1 on 2023-05-18 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0005_rename_disease_diseasehistory_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=100, unique=True)),
                ('english_name', models.CharField(max_length=100, unique=True)),
                ('symptom_groups', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disease.symptomsgroup')),
            ],
        ),
    ]