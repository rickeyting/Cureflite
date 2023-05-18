# Generated by Django 4.2.1 on 2023-05-13 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BadHabits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=100, unique=True)),
                ('english_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=100, unique=True)),
                ('english_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=100, unique=True)),
                ('english_name', models.CharField(max_length=100, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('male_age_max', models.IntegerField(default=999, null=True)),
                ('male_age_min', models.IntegerField(default=0, null=True)),
                ('female_age_max', models.IntegerField(default=999, null=True)),
                ('female_age_min', models.IntegerField(default=0, null=True)),
                ('family_history', models.BooleanField(default=False)),
                ('bad_habits', models.ManyToManyField(to='disease.badhabits')),
                ('clinic', models.ManyToManyField(to='disease.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=100, unique=True)),
                ('english_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('bad_habits', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disease.badhabits')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('symptoms', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disease.symptoms')),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('changes', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.disease')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='disease',
            name='symptoms',
            field=models.ManyToManyField(to='disease.symptoms'),
        ),
    ]
