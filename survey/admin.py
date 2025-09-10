from django.contrib import admin
from .models import QuestionnaireResponse

@admin.register(QuestionnaireResponse)
class QuestionnaireResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "sex", "vas_pain", "satisfaction", "ambulation", "created_at")
    list_filter = ("sex", "ambulation", "created_at")
    search_fields = ("name",)


# Register your models here.
