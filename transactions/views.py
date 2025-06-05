from django.shortcuts import render

from django.http import HttpResponse
from .models import Transaction, Category, Status, Kind, SubCategory
  
def index(request):
    transactions = Transaction.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    kinds = Kind.objects.all()

    return render(request, 'index.html',{
        'transactions': transactions,
        'categories': categories,
        'statuses': statuses,
        'kinds': kinds,
        })

def create(request):
    subcats = SubCategory.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    kinds = Kind.objects.all()

    return render(request, 'create.html',{
        'categories': categories,
        'statuses': statuses,
        'kinds': kinds,
        'subcats': subcats,
        })

def form(request):

    categories = Category.objects.all()
    statuses = Status.objects.all()
    kinds = Kind.objects.all()

    return render(request, 'form.html',{
        'categories': categories,
        'statuses': statuses,
        'kinds': kinds,
        })
