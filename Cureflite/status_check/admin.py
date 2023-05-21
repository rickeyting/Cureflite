from django.contrib import admin
from .models import SearchHistory, UnknownSymptoms, UnknownHabit

# Register your models here.
admin.site.register(SearchHistory)
admin.site.register(UnknownSymptoms)
admin.site.register(UnknownHabit)
