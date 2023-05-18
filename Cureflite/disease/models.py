from django.db import models
from django.http import QueryDict
from django.contrib.auth import get_user_model
from members.models import User
import json
import ast
User = get_user_model()


# Create your models here.
class Clinic(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chinese_name


class Symptoms(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chinese_name

    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the object is being created (no primary key exists)
        super().save(*args, **kwargs)

        if created:
            new_group = SymptomsGroup.objects.create(chinese_name=self.chinese_name)
            new_group.symptoms.add(self)


class SymptomsGroup(models.Model):
    chinese_name = models.CharField(max_length=100, null=True)
    symptoms = models.ManyToManyField(Symptoms)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chinese_name

    def get_dic(self):
        group_dic = {
            'chinese_name': self.chinese_name,
            'symptoms': [] + list(self.symptoms.values_list('chinese_name', flat=True)),
        }
        return group_dic

    def adjust_symptoms(self, new_symptom_ids, rename=False):
        # Convert the input symptom IDs to integers
        new_symptom_ids = [int(symptom_id) for symptom_id in new_symptom_ids]

        # Step 1: Create new groups for removed symptoms
        removed_symptoms = self.symptoms.exclude(id__in=new_symptom_ids)
        for symptom in removed_symptoms:
            new_group = SymptomsGroup.objects.create(chinese_name=symptom.chinese_name)
            new_group.symptoms.add(symptom)


        # Step 2: Remove symptoms from the current group if not in the input list
        self.symptoms.remove(*self.symptoms.exclude(id__in=new_symptom_ids))
        self.chinese_name = rename
        self.save()

        # Step 3: Add new symptoms to the current group if not already in the group
        self.symptoms.add(*Symptoms.objects.filter(id__in=new_symptom_ids).exclude(symptomsgroup=self))

        # Step 4: Remove added symptoms from other groups and remove empty groups
        for symptom_id in new_symptom_ids:
            symptom = Symptoms.objects.get(id=symptom_id)
            other_groups = SymptomsGroup.objects.filter(symptoms=symptom).exclude(pk=self.pk)
            for group in other_groups:
                group.symptoms.remove(symptom)
                if group.symptoms.count() == 0:
                    group.delete()

        if self.symptoms.count() == 0:
            self.delete()

class BadHabits(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chinese_name

    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the object is being created (no primary key exists)
        super().save(*args, **kwargs)

        if created:
            new_group = BadHabitsGroup.objects.create(chinese_name= self.chinese_name)
            new_group.bad_habits.add(self)


class BadHabitsGroup(models.Model):
    chinese_name = models.CharField(max_length=100, null=True)
    bad_habits = models.ManyToManyField(BadHabits)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chinese_name

    def get_dic(self):
        group_dic = {
            'chinese_name': self.chinese_name,
            'bad_habits': [] + list(self.bad_habits.values_list('chinese_name', flat=True)),
        }
        return group_dic

    def adjust_bad_habit(self, new_bad_habit_ids, rename=False):
        # Convert the input bad_habits IDs to integers
        new_bad_habit_ids = [int(bad_habit_id) for bad_habit_id in new_bad_habit_ids]

        # Step 1: Create new groups for removed bad_habits
        removed_bad_habits = self.bad_habits.exclude(id__in=new_bad_habit_ids)
        for bad_habit in removed_bad_habits:
            new_group = BadHabitsGroup.objects.create(chinese_name=bad_habit.chinese_name)
            new_group.bad_habits.add(bad_habit)

        # Step 2: Remove bad_habits from the current group if not in the input list
        self.bad_habits.remove(*self.bad_habits.exclude(id__in=new_bad_habit_ids))
        self.chinese_name = rename
        self.save()


        # Step 3: Add new bad_habits to the current group if not already in the group
        self.bad_habits.add(*BadHabits.objects.filter(id__in=new_bad_habit_ids).exclude(badhabitsgroup=self))

        # Step 4: Remove added bad_habits from other groups and remove empty groups
        for bad_habit_id in new_bad_habit_ids:
            bad_habit = BadHabits.objects.get(id=bad_habit_id)
            other_groups = BadHabitsGroup.objects.filter(bad_habits=bad_habit).exclude(pk=self.pk)
            for group in other_groups:
                group.bad_habits.remove(bad_habit)
                if group.bad_habits.count() == 0:
                    group.delete()

        if self.bad_habits.count() == 0:
            self.delete()


class Disease(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100, null=True)
    symptoms = models.ManyToManyField(Symptoms)
    bad_habits = models.ManyToManyField(BadHabits)
    created_date = models.DateTimeField(auto_now_add=True)
    male_age_max = models.IntegerField(default=999, null=True)
    male_age_min = models.IntegerField(default=0, null=True)
    female_age_max = models.IntegerField(default=999, null=True)
    female_age_min = models.IntegerField(default=0, null=True)
    clinic = models.ManyToManyField(Clinic)
    family_history = models.BooleanField(default=False)

    def __str__(self):
        return self.chinese_name  # Return the Chinese name when the object is referenced

    def get_dic(self):
        disease_dic = {
            'chinese_name': self.chinese_name,
            'symptoms': [] + list(self.symptoms.values_list('chinese_name', flat=True)),
            'bad_habits': [] + list(self.bad_habits.values_list('chinese_name', flat=True)),
            'male_age_min': self.male_age_min or 0,
            'male_age_max': self.male_age_max or 999,
            'female_age_min': self.female_age_min or 0,
            'female_age_max': self.female_age_max or 999,
            'clinic': [] + list(self.clinic.values_list('chinese_name', flat=True)),
            'family_history': self.family_history or False,
        }
        return disease_dic

    def adjust_disease(self, new_data):
        self.male_age_min = new_data.get('male_age_min')
        self.male_age_max = new_data.get('male_age_max')
        self.female_age_min = new_data.get('female_age_min')
        self.female_age_max = new_data.get('female_age_max')

        if new_data.get('family_history') in ['on', 'TRUE', 'T']:
            self.family_history = True
        else:
            self.family_history = False
        self.save()


        if isinstance(new_data, QueryDict):
            symptoms = new_data.getlist('symptoms', [])
            bad_habits = new_data.getlist('bad_habits', [])
            clinics = new_data.getlist('clinic', [])
        else:
            symptoms = new_data.get('symptoms')
            bad_habits = new_data.get('bad_habits')
            clinics = new_data.get('clinic')

        # Get the related objects from the related manager
        all_symptoms = set(str(item[0]) for item in self.symptoms.values_list('chinese_name')) | set(symptoms)
        all_bad_habits = set(str(item[0]) for item in self.bad_habits.values_list('chinese_name')) | set(bad_habits)
        all_clinics = set(str(item[0]) for item in self.clinic.values_list('chinese_name')) | set(clinics)

        add_symptoms = set(symptoms) - set(str(item[0]) for item in self.symptoms.values_list('chinese_name'))
        add_bad_habits = set(bad_habits) - set(str(item[0]) for item in self.bad_habits.values_list('chinese_name'))
        add_clinics = set(clinics) - set(str(item[0]) for item in self.clinic.values_list('chinese_name'))

        remove_symptoms = set(str(item[0]) for item in self.symptoms.values_list('chinese_name')) - set(symptoms)
        remove_bad_habits = set(str(item[0]) for item in self.bad_habits.values_list('chinese_name')) - set(bad_habits)
        remove_clinics = set(str(item[0]) for item in self.clinic.values_list('chinese_name')) - set(clinics)
        # Add & remove symptoms
        for symptom_name in add_symptoms:
            symptom, created = Symptoms.objects.get_or_create(chinese_name=symptom_name)
            self.symptoms.add(symptom)

        for symptom_name in remove_symptoms:
            symptom = Symptoms.objects.get(chinese_name=symptom_name)
            self.symptoms.remove(symptom)

        # Add & remove bad_habits
        for bad_habit_name in add_bad_habits:
            bad_habit, created = BadHabits.objects.get_or_create(chinese_name=bad_habit_name)
            self.bad_habits.add(bad_habit)

        for bad_habit_name in remove_bad_habits:
            bad_habit = BadHabits.objects.get(chinese_name=bad_habit_name)
            self.bad_habits.remove(bad_habit)

        # Add & remove clinic
        for clinic_name in add_clinics:
            clinic, created = Clinic.objects.get_or_create(chinese_name=clinic_name)
            self.clinic.add(clinic)

        for clinic_name in remove_clinics:
            clinic = Clinic.objects.get(chinese_name=clinic_name)
            self.clinic.remove(clinic)


class DiseaseHistory(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    changes = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def get_changes_dict(self):
        try:
            history_dict = ast.literal_eval(self.changes)
            history_dict['title'] = self.title
            history_dict['timestamp'] = self.timestamp
            return history_dict
        except json.JSONDecodeError:
            # Handle invalid JSON if needed
            return {}

    def save_info(self, new, old):
        changed = {}
        for key, value in old.items():
            add = []
            remove = []
            if isinstance(value, list):
                all_item = list(set(new[key]) | set(value))
                add = list(set(new[key]) - set(value))
                remove = list(set(value) - set(new[key]))
            else:
                new_value = new.get(key)
                all_item = [new_value]
                if str(new_value) != str(value):
                    add = [new_value]
            changed[key] = {'all_item': all_item, 'add': add, 'remove': remove}
        all_empty = all(len(value['add']) == 0 and len(value['remove']) == 0 for value in changed.values())
        if not all_empty:
            self.changes = changed
            self.save()
        else:
            self.delete()

    def delete_info(self, old):
        changed = {}
        for key, value in old.items():
            add = []
            if isinstance(value, list):
                all_item = value
                remove = value
            else:
                all_item = [value]
                remove = [value]

            changed[key] = {'all_item': all_item, 'add': add, 'remove': remove}
        self.changes = changed
        self.save()


class BodyParts(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100, unique=True)
    symptom_groups = models.ManyToManyField(SymptomsGroup)

    def __str__(self):
        return self.chinese_name

    def get_dic(self):
        group_dic = {
            'chinese_name': self.chinese_name,
            'symptom_groups': [] + list(self.symptom_groups.values_list('chinese_name', flat=True)),
        }
        return group_dic

    def adjust_data(self, new_symptom_groups_ids):
        # Convert the input symptom groups IDs to integers
        new_symptom_groups_ids = [int(symptom_group_id) for symptom_group_id in new_symptom_groups_ids]

        # Step 1: Remove symptom groups from the current group if not in the input list
        self.symptom_groups.remove(*self.symptom_groups.exclude(id__in=new_symptom_groups_ids))

        # Step 2: Add new symptom groups to the current group if not already in the group
        self.symptom_groups.add(*SymptomsGroup.objects.filter(id__in=new_symptom_groups_ids))

        self.save()


class SearchHistory(models.Model):
    symptoms = models.ForeignKey(Symptoms, on_delete=models.PROTECT)
    bad_habits = models.ForeignKey(BadHabits, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search History {self.pk}"
