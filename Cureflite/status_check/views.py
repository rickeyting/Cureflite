from django.shortcuts import render
from disease.models import BodyParts, BadHabitsGroup
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SearchHistory


# Create your views here.
def status_check(request):
    body_groups = BodyParts.objects.all()
    bad_habit_groups = BadHabitsGroup.objects.all()
    return render(request, 'status/status_check.html', {'body_groups': body_groups, 'bad_habit_groups': bad_habit_groups})


def get_result(request):
    if request.method == 'POST':
        symptoms_group = request.POST.getlist('symptoms_group')
        habits_group = request.POST.getlist('habits_group')
        if not symptoms_group and not habits_group:
            messages.error(request, '請輸入病症或行為')
            return redirect('status_check')
        else:
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            creator = None if request.user.is_anonymous else request.user
            new_history = SearchHistory.objects.create(gender=gender, age=age, creator=creator)
            new_history.save_data(symptoms_group, habits_group)
            result = new_history.get_result()
            if len(result) == 0:
                messages.error(request, '抱歉，資料庫資訊不足無法獲取相關資料')
                return redirect('status_check')
            else:
                return render(request, 'status/status_result.html', {'result': result})
        return redirect('status_check')