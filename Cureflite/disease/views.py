import csv
import io

from django.shortcuts import render, redirect
from .models import Disease, Symptoms, BadHabits, Clinic, DiseaseHistory, SymptomsGroup, BadHabitsGroup, BodyParts
from status_check.models import UnknownSymptoms, UnknownHabit
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()


# Create functions here
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def update_diseases(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        csv_data = csv_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(csv_data))
        cleaned_data = {}
        for row in reader:
            cleaned_row = {}
            for key, value in row.items():
                cleaned_key = key.strip('\ufeff')  # Remove the BOM character from the field name
                cleaned_row[cleaned_key] = value.strip()  # Remove leading/trailing whitespace from the field value

            chinese_name = cleaned_row['chinese_name']
            new_disease = cleaned_data.get('chinese_name')
            if new_disease:
                if new_disease == chinese_name:
                    if cleaned_row['symptoms']:
                        cleaned_data['symptoms'].append(cleaned_row['symptoms'])
                    if cleaned_row['bad_habits']:
                        cleaned_data['bad_habits'].append(cleaned_row['bad_habits'])
                    if cleaned_row['clinic']:
                        cleaned_data['clinic'].append(cleaned_row['clinic'])
                else:
                    cleaned_data['symptoms'] = list(set(cleaned_data['symptoms']))
                    cleaned_data['bad_habits'] = list(set(cleaned_data['bad_habits']))
                    cleaned_data['clinic'] = list(set(cleaned_data['clinic']))

                    try:
                        current_disease = Disease.objects.get(chinese_name=new_disease)
                    except:
                        current_disease = Disease.objects.create(chinese_name=new_disease)
                    old_data = current_disease.get_dic()
                    current_disease.adjust_disease(cleaned_data)
                    new_data = current_disease.get_dic()
                    new_history = DiseaseHistory.objects.create(title='疾病', user=request.user)
                    new_history.save_info(new_data, old_data)
                    cleaned_data = {}
            else:
                cleaned_data['chinese_name'] = chinese_name
                cleaned_data['symptoms'] = [cleaned_row['symptoms']] if cleaned_row['symptoms'] else []
                cleaned_data['bad_habits'] = [cleaned_row['bad_habits']] if cleaned_row['bad_habits'] else []
                cleaned_data['male_age_min'] = int(cleaned_row['male_age_min']) if cleaned_row['male_age_min'] else 0
                cleaned_data['male_age_max'] = int(cleaned_row['male_age_max']) if cleaned_row['male_age_max'] else 999
                cleaned_data['female_age_min'] = int(cleaned_row['female_age_min']) if cleaned_row['female_age_min'] else 0
                cleaned_data['female_age_max'] = int(cleaned_row['female_age_max']) if cleaned_row['female_age_max'] else 999
                cleaned_data['clinic'] = [cleaned_row['clinic']] if cleaned_row['clinic'] else []
                cleaned_data['family_history'] = 'T' if cleaned_row['family_history'] else 'F'
            # You can add any additional processing or error handling here

        return redirect('disease_overview')  # Redirect to a relevant URL after updating the diseases

    return render(request, 'disease_overview.html')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def download_diseases(request):
    # Retrieve all diseases from the database
    diseases = Disease.objects.all()

    # Create a response with the CSV file
    output = io.StringIO()
    response = HttpResponse(output.getvalue().encode('utf-8-sig'), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="diseases.csv"'

    # Create a CSV writer and write the header row
    writer = csv.writer(response)
    writer.writerow(['chinese_name', 'clinic', 'symptoms', 'male_age_min', 'male_age_max', 'female_age_min', 'female_age_max', 'bad_habits', 'family_history'])

    # Write each disease as a row in the CSV file
    for disease in diseases:
        max_symptoms = len(disease.symptoms.all())
        max_bad_habits = len(disease.bad_habits.all())
        max_clinic = len(disease.clinic.all())
        max_items = max(max_symptoms, max_bad_habits, max_clinic)
        for i in range(max_items):
            all_clinic = disease.clinic.all()
            if i < len(all_clinic):
                clinic = all_clinic[i]
                clinic_chinese_name = clinic.chinese_name if clinic else ''
            else:
                clinic_chinese_name = ''
            all_symptoms = disease.symptoms.all()
            if i < len(all_symptoms):
                symptoms = all_symptoms[i]
                symptoms_chinese_name = symptoms.chinese_name if symptoms else ''
            else:
                symptoms_chinese_name = ''
            all_bad_habits = disease.bad_habits.all()
            if i < len(all_bad_habits):
                bad_habits = all_bad_habits[i]
                bad_habits_chinese_name = bad_habits.chinese_name if bad_habits else ''
            else:
                bad_habits_chinese_name = ''

            if i == 0:
                writer.writerow([
                    disease.chinese_name,
                    clinic_chinese_name,
                    symptoms_chinese_name,
                    disease.male_age_min,
                    disease.male_age_max,
                    disease.female_age_min,
                    disease.female_age_max,
                    bad_habits_chinese_name,
                    disease.family_history,
                ])
            else:
                writer.writerow([
                    disease.chinese_name,
                    clinic_chinese_name,
                    symptoms_chinese_name,
                    '',
                    '',
                    '',
                    '',
                    bad_habits_chinese_name,
                    '',
                ])
    return response


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def disease_overview(request, disease_id=None):
    diseases = Disease.objects.order_by('-created_date')
    symptoms = Symptoms.objects.order_by('-created_date')
    clinics = Clinic.objects.order_by('-created_date')
    bad_habits = BadHabits.objects.order_by('-created_date')
    disease_history = DiseaseHistory.objects.order_by('-timestamp')[:3]
    body_parts = BodyParts.objects.annotate(symptom_group_count=Count('symptom_groups'))
    unknown_symptoms = UnknownSymptoms.objects.count()
    unknown_habits = UnknownHabit.objects.count()

    disease_count = diseases.count()
    symptom_count = symptoms.count()
    bad_habit_count = bad_habits.count()
    clinics_count = clinics.count()

    disease_histories = []
    for i in disease_history:
        history_dic = i.get_changes_dict()
        disease_histories.append([history_dic, i])
    return render(request, 'disease_overview.html', {
        'diseases': diseases,
        'history_content': disease_histories,
        'disease_count': disease_count,
        'symptom_count': symptom_count,
        'bad_habit_count': bad_habit_count,
        'clinics_count': clinics_count,
        'body_parts': body_parts,
        'unknown_symptoms': unknown_symptoms,
        'unknown_habits': unknown_habits,
    })


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def disease_history_info(request):
    disease_history = DiseaseHistory.objects.order_by('-timestamp')
    disease_histories = []
    for i in disease_history:
        history_dic = i.get_changes_dict()
        disease_histories.append([history_dic, i])
    return render(request, 'disease_history_info.html', {'history_content': disease_histories})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def clinic_info(request, clinic_id=None):
    clinics = Clinic.objects.order_by('-created_date')
    diseases = Disease.objects.order_by('-created_date')
    if clinic_id == None:
        current_clinic = clinics.first()
    else:
        current_clinic = Clinic.objects.get(id=clinic_id)
    return render(request, 'clinic_info.html', {'clinics': clinics, 'diseases': diseases, 'current_clinic':current_clinic})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def add_clinic(request, clinic_id):
    if request.method == 'POST':
        changed_disease_ids = [int(item_id) for item_id in request.POST.getlist('diseases')]
        disease_ids = list(Disease.objects.filter(clinic__id=clinic_id).values_list('id', flat=True))
        increase_ids = set(changed_disease_ids) - set(disease_ids)
        decrease_ids = set(disease_ids) - set(changed_disease_ids)
        clinic_name = Clinic.objects.get(id=clinic_id).chinese_name
        # add clinic
        for disease_id in increase_ids:
            check_disease = Disease.objects.get(id=disease_id)
            disease_dic = check_disease.get_dic()
            disease_dic['clinic'].append(clinic_name)

            old_data = check_disease.get_dic()
            check_disease.adjust_disease(disease_dic)
            new_data = check_disease.get_dic()
            new_history = DiseaseHistory.objects.create(title='疾病', user=request.user)
            new_history.save_info(new_data, old_data)


        # subtract clinic
        for disease_id in decrease_ids:
            check_disease = Disease.objects.get(id=disease_id)
            disease_dic = check_disease.get_dic()
            disease_dic['clinic'].remove(clinic_name)

            old_data = check_disease.get_dic()
            check_disease.adjust_disease(disease_dic)
            new_data = check_disease.get_dic()
            new_history = DiseaseHistory.objects.create(title='疾病', user=request.user)
            new_history.save_info(new_data, old_data)

        return redirect('clinic_info', clinic_id=clinic_id)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def symptom_info(request, symptom_group_id=None):
    symptomsgroup = SymptomsGroup.objects.order_by('-created_date')
    try:
        current_symptomsgroup = SymptomsGroup.objects.get(id=symptom_group_id)
    except:
        current_symptomsgroup = symptomsgroup.first()
    return render(request, 'symptom_info.html', {'symptomsgroups': symptomsgroup, 'current_symptomsgroup': current_symptomsgroup})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def add_symptom(request, symptom_group_id):
    if request.method == 'POST':
        new_symptoms = request.POST.getlist('group')
        new_name = request.POST.get('chinese_name')
        current_symptomsgroup = SymptomsGroup.objects.get(id=symptom_group_id)
        old_group = current_symptomsgroup.get_dic()
        current_symptomsgroup.adjust_symptoms(new_symptoms, new_name)
        new_history = DiseaseHistory.objects.create(title='病症群組異動', user=request.user)
        try:
            new_group = SymptomsGroup.objects.get(id=symptom_group_id).get_dic()
            new_history.save_info(new_group, old_group)
        except:
            new_history.delete_info(old_group)
        return redirect('symptom_info', symptom_group_id=symptom_group_id)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def bad_habit_info(request, bad_habit_group_id=None):
    bad_habit_group = BadHabitsGroup.objects.order_by('-created_date')
    try:
        current_bad_habit_group = BadHabitsGroup.objects.get(id=bad_habit_group_id)
    except:
        current_bad_habit_group = bad_habit_group.first()
    return render(request, 'bad_habit_info.html', {'bad_habit_groups': bad_habit_group, 'current_bad_habit_group': current_bad_habit_group})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def add_bad_habit(request, bad_habit_group_id):
    if request.method == 'POST':
        new_bad_habits = request.POST.getlist('group')
        new_name = request.POST.get('chinese_name')
        current_bad_habit_group = BadHabitsGroup.objects.get(id=bad_habit_group_id)
        old_group = current_bad_habit_group.get_dic()
        current_bad_habit_group.adjust_bad_habit(new_bad_habits, new_name)
        new_history = DiseaseHistory.objects.create(title='行為群組異動', user=request.user)
        try:
            new_group = BadHabitsGroup.objects.get(id=bad_habit_group_id).get_dic()
            new_history.save_info(new_group, old_group)
        except:
            new_history.delete_info(old_group)
        return redirect('bad_habit_info', bad_habit_group_id=bad_habit_group_id)


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def diseases_info(request, diseases_info_id=None):
    diseases = Disease.objects.order_by('-created_date')
    clinics = Clinic.objects.order_by('-created_date')
    try:
        current_disease = Disease.objects.get(id=diseases_info_id)
    except:
        return render(request, 'diseases_info.html', {'diseases': diseases, 'clinics': clinics})
    return render(request, 'diseases_info.html', {'diseases': diseases, 'clinics': clinics, 'current_disease': current_disease})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def add_diseases(request, diseases_info_id=None):
    if request.method == 'POST':
        disease_name = request.POST.get('chinese_name')
        if not diseases_info_id:
            current_disease = Disease.objects.create(chinese_name=disease_name)
        else:
            current_disease = Disease.objects.get(id=diseases_info_id)
        old_data = current_disease.get_dic()
        current_disease.adjust_disease(request.POST)
        new_data = current_disease.get_dic()
        new_history = DiseaseHistory.objects.create(title='疾病資料異動', user=request.user)
        new_history.save_info(new_data, old_data)
        return redirect('disease_info', diseases_info_id=current_disease.id)

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def delete_diseases(request, diseases_info_id):
    current_disease = get_object_or_404(Disease, id=diseases_info_id)
    new_history = DiseaseHistory.objects.create(title='疾病資料異動', user=request.user)
    new_history.delete_info(current_disease.get_dic())
    current_disease.delete()
    diseases = Disease.objects.order_by('-created_date')
    top_diseases = diseases.first()
    return redirect('disease_info', diseases_info_id=top_diseases.id)

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def body_part_info(request, body_part_id=None):
    body_parts = BodyParts.objects.all()
    symptom_groups = SymptomsGroup.objects.order_by('-created_date')
    try:
        current_body_part = BodyParts.objects.get(id=body_part_id)
    except:
        current_body_part = body_parts.first()
    grouped_symptom_groups = []
    for symptom_group in symptom_groups:
        for body_part in body_parts:
            if symptom_group in body_part.symptom_groups.all():
                if symptom_group not in grouped_symptom_groups:
                    grouped_symptom_groups.append(symptom_group)
    return render(request, 'body_part_info.html', {'symptom_groups': symptom_groups,
                                                   'grouped_symptom_groups': grouped_symptom_groups,
                                                   'body_parts': body_parts,
                                                   'current_body_part': current_body_part})


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def add_body_part(request, body_part_id):
    if request.method == 'POST':
        new_body_parts = request.POST.getlist('group')
        current_body_part = BodyParts.objects.get(id=body_part_id)
        old_group = current_body_part.get_dic()
        current_body_part.adjust_data(new_body_parts)
        new_history = DiseaseHistory.objects.create(title='身體部位異動', user=request.user)
        new_group = BodyParts.objects.get(id=body_part_id).get_dic()
        new_history.save_info(new_group, old_group)
        return redirect('body_part_info', body_part_id=body_part_id)