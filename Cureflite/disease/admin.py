from django.contrib import admin
from .models import Disease, BadHabits, Symptoms, Clinic, DiseaseHistory, BadHabitsGroup, SymptomsGroup, BodyParts

# Register your models here.
admin.site.register(Disease)
admin.site.register(BadHabits)
admin.site.register(Symptoms)
admin.site.register(Clinic)
admin.site.register(DiseaseHistory)
admin.site.register(BadHabitsGroup)
admin.site.register(SymptomsGroup)
admin.site.register(BodyParts)
