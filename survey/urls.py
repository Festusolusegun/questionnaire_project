from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.questionnaire_view, name="questionnaire"),
    path('thank-you/', views.thank_you_view, name="thank_you"),
    path('results/', views.results_view, name="results"),
    path('export-csv/', views.export_responses_csv, name='export_responses_csv'),

    # login/logout
    path('login/', auth_views.LoginView.as_view(template_name='survey/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


