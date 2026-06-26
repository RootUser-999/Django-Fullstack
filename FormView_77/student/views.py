from django.shortcuts import render
from .forms import StudentForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class FormViewstd(FormView):
    template_name='student/std.html'
    form_class=StudentForm
    success_url='/thankyou/'
    def form_valid(self,form):
        form.save()




class ThankTemplateView(TemplateView):
    template_name='student/thankyou.html'
    
    