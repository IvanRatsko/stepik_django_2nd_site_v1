"""stepik_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from vacancies.views import CompanyView
from vacancies.views import MainView
from vacancies.views import VacanciesCatView
from vacancies.views import VacanciesView
from vacancies.views import VacancyView
from vacancies.views import custom_handler404
from vacancies.views import custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:specialty>', VacanciesCatView.as_view()),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view()),
    path('companies/<int:company_id>', CompanyView.as_view()),

]

handler404 = custom_handler404
handler500 = custom_handler500
