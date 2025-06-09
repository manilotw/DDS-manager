from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import Transaction, Category, Status, Kind, SubCategory
  
def index(request):

    transactions = Transaction.objects.all()

    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')
    status = request.GET.get('status')
    kind = request.GET.get('kind')
    category = request.GET.get('category')

    if date_start:
        transactions = transactions.filter(date__gte=date_start)
    if date_end:
        transactions = transactions.filter(date__lte=date_end)
    if status and status != 'Все':
        transactions = transactions.filter(status_id=status)
    if kind and kind != 'Все':
        transactions = transactions.filter(kind_id=kind)
    if category and category != 'Все':
        transactions = transactions.filter(category_id=category)

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
    if request.method == 'POST':
        data = request.POST.dict()

        Transaction.objects.create(
            date=data.get('record_date'),
            status=Status.objects.get(id=data.get('record_status')),
            kind=Kind.objects.get(id=data.get('record_type')),
            category=Category.objects.get(id=data.get('record_category')),
            amount=data.get('record_amount'),
            comment=data.get('record_comment')
        )

        return redirect('home')

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
    transaction = get_object_or_404(Transaction, id=pk)

    if request.method == 'POST':
        transaction.date = request.POST.get('record_date')
        transaction.status = Status.objects.get(id=request.POST.get('record_status'))
        transaction.kind = Kind.objects.get(id=request.POST.get('record_type'))
        transaction.category = Category.objects.get(id=request.POST.get('record_category'))
        subcategory_id = request.POST.get('record_subcategory')
        subcategory = SubCategory.objects.get(id=subcategory_id)
        transaction.category.subcategories.set([subcategory])  
        transaction.amount = request.POST.get('record_amount')
        transaction.comment = request.POST.get('record_comment')
        transaction.save()
        return redirect('home')

    statuses = Status.objects.all()
    kinds = Kind.objects.all()  
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

    return render(request, 'edit.html', {
        'transaction': transaction,
        'statuses': statuses,
        'kinds': kinds,
        'categories': categories,
        'subcats': subcats
    })

