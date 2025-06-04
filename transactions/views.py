from django.shortcuts import render

from django.http import HttpResponse
from .models import Transaction
  
def index(request):
    transactions = Transaction.objects.all()

    return render(request, 'index.html', {'transactions': transactions})

def create(request):
    return render(request, 'create.html')

def form(request):
    return render(request, 'form.html')
