from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *

def pop_entry(request):
    form = PopEntryForm(request.POST)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'pop_entry.html', context)
