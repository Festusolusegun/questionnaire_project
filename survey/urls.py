from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaire_view, name="questionnaire"),
    path('thank-you/', views.thank_you_view, name="thank_you"),
    path('results/', views.results_view, name="results"),
    path('export-csv/', views.export_responses_csv, name='export_responses_csv'),
]



