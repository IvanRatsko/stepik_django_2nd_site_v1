from django.http import HttpResponseNotFound
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from vacancies.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = "vacancies/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specialties"] = Specialty.objects.all()
        context["companies"] = Company.objects.all()
        context["vacancies"] = Vacancy.objects.all()
        return context


class CompanyView(TemplateView):
    template_name = "vacancies/company.html"

    def get_context_data(self, company_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies"] = Vacancy.objects.filter(company__id=company_id)
        context["title"] = Company.objects.get(id=company_id).name
        context['prev_url'] = self.request.META.get('HTTP_REFERER')
        return context


class VacanciesCatView(TemplateView):
    template_name = "vacancies/vacancies.html"

    def get_context_data(self, specialty, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacancies"] = Vacancy.objects.filter(specialty__code=specialty)
        context["title"] = Specialty.objects.get(code=specialty).title
        return context


class VacanciesView(ListView):
    model = Vacancy
    queryset = Vacancy.objects.select_related('company').all()
    context_object_name = "vacancies"
    template_name = "vacancies/vacancies.html"
    title = "Все вакансии"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class VacancyView(DetailView):
    template_name = "vacancies/vacancy.html"
    pk_url_kwarg = 'vacancy_id'
    model = Vacancy
    queryset = Vacancy.objects.select_related('company').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_url'] = self.request.META.get('HTTP_REFERER')
        return context


def custom_handler404(request):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseNotFound('Ошибка 500')
