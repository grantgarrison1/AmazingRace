"""
URL configuration for yL_Somret_V project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from leaders import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.leadersHome, name='leadersHome'),
    path('', views.leadersHome, name='Home'),  # Add this line
    path('makeQuestions/', views.make_questions, name='makeQuestions'),
    path('savedQuestions/', views.saved_races, name='saved_races'),
    path('editRace/<int:race_id>/', views.edit_race, name='editRace'),
    path('launchRace/<int:race_id>/', views.launch_race, name='launchRace'),
    path('delete_race/<int:race_id>/', views.delete_race, name='delete_race'),

    


]
