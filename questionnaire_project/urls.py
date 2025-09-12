from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views   # 👈 import Django’s auth views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('survey.urls')),   # your survey app routes

    # 🔑 Authentication routes
# Authentication routes (use default template location: registration/login.html)
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]




