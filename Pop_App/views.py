from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *

def pop_entry(request):

    form = PopEntryForm()
    return render(request, 'pop_entry.html', {"form": form})
