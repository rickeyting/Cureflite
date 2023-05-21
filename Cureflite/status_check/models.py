from django.db import models
from disease.models import Symptoms, BadHabits, SymptomsGroup, BadHabitsGroup, Disease
from members.models import GENDER_CHOICES
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()


# Create your models here.
class SearchHistory(models.Model):
    symptom_groups = models.ManyToManyField(SymptomsGroup)
    bad_habit_groups = models.ManyToManyField(BadHabitsGroup)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search History {self.pk}"

    def save_data(self, search_symptoms, search_habits):
        existing_symptom_groups = SymptomsGroup.objects.filter(chinese_name__in=search_symptoms)
        for symptom_group in search_symptoms:
            if symptom_group in existing_symptom_groups.values_list('chinese_name', flat=True):
                symptom_group_obj = SymptomsGroup.objects.get(chinese_name=symptom_group)
                self.symptom_groups.add(symptom_group_obj)
            else:
                try:
                    existing_symptom = Symptoms.objects.get(chinese_name=symptom_group)
                    group = existing_symptom.symptomsgroup_set.first()
                    self.symptom_groups.add(group)
                except:
                    try:
                        unknown_symptom = UnknownSymptoms.objects.get(chinese_name=symptom_group)
                    except:
                        UnknownSymptoms.objects.create(chinese_name=symptom_group)

        existing_habit_groups = BadHabitsGroup.objects.filter(chinese_name__in=search_habits)
        for habit_group in search_habits:
            if habit_group in existing_habit_groups.values_list('chinese_name', flat=True):
                habit_group_obj = BadHabitsGroup.objects.get(chinese_name=habit_group)
                self.bad_habit_groups.add(habit_group_obj)
            else:
                try:
                    existing_habit = BadHabits.objects.get(chinese_name=habit_group)
                    group = existing_habit.badhabitsgroup_set.first()
                    self.bad_habit_groups.add(group)
                except:
                    try:
                        unknown_habit = UnknownHabit.objects.get(chinese_name=habit_group)
                    except:
                        UnknownHabit.objects.create(chinese_name=habit_group)

    def get_result(self):
        if self.symptom_groups.exists() or self.bad_habit_groups.exists():
            matching_diseases = Disease.objects.all()

            # Match at least one symptom from any of the symptom groups
            for symptom_group in self.symptom_groups.all():
                matching_diseases = matching_diseases.filter(symptoms__in=symptom_group.symptoms.all())

            # Match at least one bad habit from each of the bad habit groups
            for habit_group in self.bad_habit_groups.all():
                matching_diseases = matching_diseases.filter(bad_habits__in=habit_group.bad_habits.all())

            matching_diseases = matching_diseases.distinct()
            clinic_counts = matching_diseases.values('clinic__id', 'clinic__chinese_name').annotate(count=Count('clinic__id'))
            clinic_dict = {clinic_count['clinic__chinese_name']: clinic_count['count'] for clinic_count in clinic_counts}
            sorted_clinic_dict = dict(sorted(clinic_dict.items(), key=lambda x: x[1], reverse=True))
            return sorted_clinic_dict
        else:
            return {}


class UnknownSymptoms(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)


class UnknownHabit(models.Model):
    chinese_name = models.CharField(max_length=100, unique=True)
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)