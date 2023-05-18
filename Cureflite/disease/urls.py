from django.urls import path
from . import views


urlpatterns = [
    path('disease-overview/', views.disease_overview, name='disease_overview'),
    path('disease-overview/update-diseases/', views.update_diseases, name='update_diseases'),
    path('disease-overview/download-diseases/', views.download_diseases, name='download_diseases'),
    path('disease-overview/clinic-info/', views.clinic_info, name='clinics_info'),
    path('disease-overview/clinic-info/<int:clinic_id>', views.clinic_info, name='clinic_info'),
    path('disease-overview/clinic-info/add_clinic/<int:clinic_id>', views.add_clinic, name='add_clinic'),
    path('disease-overview/symptom-info/', views.symptom_info, name='symptoms_info'),
    path('disease-overview/symptom-info/<int:symptom_group_id>', views.symptom_info, name='symptom_info'),
    path('disease-overview/symptom-info/add-symptom/<int:symptom_group_id>', views.add_symptom, name='add_symptom'),
    path('disease-overview/bad-habit-info/', views.bad_habit_info, name='bad_habits_info'),
    path('disease-overview/bad-habit-info/<int:bad_habit_group_id>', views.bad_habit_info, name='bad_habit_info'),
    path('disease-overview/bad-habit-info/add-bad-habit/<int:bad_habit_group_id>', views.add_bad_habit, name='add_bad_habit'),
    path('disease-overview/diseases-info/', views.diseases_info, name='diseases_info'),
    path('disease-overview/diseases-info/<int:diseases_info_id>', views.diseases_info, name='disease_info'),
    path('disease-overview/diseases-info/add-diseases/', views.add_diseases, name='add_diseases'),
    path('disease-overview/diseases-info/add-diseases/<int:diseases_info_id>', views.add_diseases, name='add_disease'),
    path('disease-overview/diseases-info/delete-diseases/<int:diseases_info_id>', views.delete_diseases, name='delete_disease'),
    path('disease-overview/body-part-info/', views.body_part_info, name='body_parts_info'),
    path('disease-overview/body-part-info/<int:body_part_id>', views.body_part_info, name='body_part_info'),
    path('disease-overview/body-part-info/add-body-part/<int:body_part_id>', views.add_body_part, name='add_body_part'),
    ]