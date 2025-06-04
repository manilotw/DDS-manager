from django.contrib import admin
from .models import Kind, Status, Category, SubCategory, Transaction

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind')
    list_filter = ('kind',)
    search_fields = ('title',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'kind', 'category', 'amount')
    list_filter = ('status', 'kind', 'category')
    search_fields = ('comment',)
    date_hierarchy = 'date'
