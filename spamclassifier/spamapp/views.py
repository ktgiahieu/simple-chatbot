from django.shortcuts import render
from django.http import HttpResponse
from spamapp import forms
from spamapp.classifier import SpamClassifer

# Create your views here.

def index(request):
    # stock_list = HistoricalPrice1Hour.objects.order_by('name')
    form = forms.FormName()
    is_spam = False
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['subject'] + ' ' + form.cleaned_data['text']
            is_spam = SpamClassifer.classify(mail)
            print(is_spam)

    response = render(request, 'index.html', {'form':form, 'is_spam':is_spam})
    return response