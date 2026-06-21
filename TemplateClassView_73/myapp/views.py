from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ={'name':'John Doe','age':30,'city':'New York','a':kwargs.get('ag')}
        print(context)
        
        return context