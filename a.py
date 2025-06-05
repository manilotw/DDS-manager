from transactions.models import Kind, Status, Category, SubCategory, Transaction
from decimal import Decimal
from django.utils import timezone
import random

# Удаляем все старые данные
Transaction.objects.all().delete()
SubCategory.objects.all().delete()
Category.objects.all().delete()
Status.objects.all().delete()
Kind.objects.all().delete()

# Создаем Kind
kinds = {
    'Доход': Kind.objects.create(title='Доход'),
    'Расход': Kind.objects.create(title='Расход'),
}

# Создаем Status
statuses = [
    Status.objects.create(title='Запланировано'),
    Status.objects.create(title='Завершено'),
    Status.objects.create(title='Отменено'),
]

# Категории и подкатегории
category_data = {
    'Доход': {
        'Зарплата': ['Основная', 'Премия'],
        'Подарки': ['От родственников', 'От друзей'],
    },
    'Расход': {
        'Маркетинг': ['Контекстная реклама', 'Баннеры'],
        'Офисные расходы': ['Канцелярия', 'Интернет'],
    }
}

categories = []
subcategories = []

# Создаем категории и подкатегории
for kind_title, cats in category_data.items():
    kind = kinds[kind_title]
    for cat_title, subcat_titles in cats.items():
        category = Category.objects.create(title=cat_title, kind=kind)
        categories.append(category)
        for sub_title in subcat_titles:
            subcat = SubCategory.objects.create(title=sub_title, category=category)
            subcategories.append(subcat)

# Создаем 10 случайных транзакций
for i in range(10):
    kind = random.choice(list(kinds.values()))
    status = random.choice(statuses)
    cat_choices = [cat for cat in categories if cat.kind == kind]
    category = random.choice(cat_choices)
    subcat_choices = [s for s in subcategories if s.category == category]
    subcategory = random.choice(subcat_choices)
    amount = Decimal(random.uniform(100, 1000)).quantize(Decimal('0.01'))
    comment = f'Тестовая транзакция #{i + 1}'

    Transaction.objects.create(
        date=timezone.now().date(),
        status=status,
        kind=kind,
        category=category,
        subcategory=subcategory,
        amount=amount,
        comment=comment
    )

print("✅ Все старые данные удалены и заново созданы, 10 транзакций добавлены с подкатегориями.")
