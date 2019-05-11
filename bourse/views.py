from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from . import forms
from . import models

# Create your views here

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def company(request):
    form = forms.company
    contents = {'form': form}
    return render(request, "form.html", context=contents)

