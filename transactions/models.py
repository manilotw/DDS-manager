from django.db import models

class Kind(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=100)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, related_name='categories')
    subcategories = models.ManyToManyField('SubCategory', related_name='cat')
    
    
    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    date = models.DateField(auto_now=True, null=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.amount} - {self.comment}'

