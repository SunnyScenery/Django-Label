# from asyncio.windows_events import NULL
from email import contentmanager
from http.client import HTTPResponse
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Label
from .forms import LabelForm

# Create your views here.

def entry(request):
    username = request.user.username
    return HttpResponseRedirect("/labelapp/%s/" % username)

def showall(request, username):
    all_labels = Label.objects.filter(user=username)
    # output = ', '.join([q.label_text for q in all_labels])
    template = loader.get_template('labelapp/index.html')
    context = {
        'username' : username,
        'labels' : all_labels,
    }
    return HttpResponse(template.render(context, request))

def addView(request, username):
    label_inst = Label()

    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            label_inst.user = username
            label_inst.label_text = form.cleaned_data['label_text']
            label_inst.save()
            return HttpResponseRedirect("/labelapp/%s/" % username)

    else:
        form = LabelForm(initial={'label_text': 'input your label'})

    template = loader.get_template('labelapp/add.html')
    context = {
        'username' : username,
        'form' : form,
    }
    return HttpResponse(template.render(context, request))

def modifyView(request, username, label):
    label_inst = Label.objects.get(user = username, label_text = label)

    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            if ('update' in request.POST):
                label_inst.user = username
                label_inst.label_text = form.cleaned_data['label_text']
                label_inst.save()
            elif ('del' in request.POST):
                label_inst.delete()
            return HttpResponseRedirect("/labelapp/%s/" % username)

    else:
        form = LabelForm(initial={'label_text': 'input your new label name'})

    template = loader.get_template('labelapp/modify.html')
    context = {
        'username' : username,
        'form' : form,
    }
    return HttpResponse(template.render(context, request))
