from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import New


class NewsView(TemplateView):
    template_name = "news/index.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["news"] = New.objects.filter(is_published=True)
        return context


class NewDetailView(DetailView):
    template_name = "news/detail.html" 
    queryset = New.objects.all()
    context_object_name = 'new'
