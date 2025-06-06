from django.shortcuts import render, get_object_or_404, redirect

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

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('home')

def edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    subcats = SubCategory.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    kinds = Kind.objects.all()

    return render(request, 'edit.html',{
        'transaction': transaction,
        'categories': categories,
        'statuses': statuses,
        'kinds': kinds,
        'subcats': subcats,
        })