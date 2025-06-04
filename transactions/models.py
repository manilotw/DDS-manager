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
    title = models.CharField(max_length=100, null=False, blank=False)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    def __str__(self):
        return f'{self.parent.title} / {self.title}' if self.parent else self.title

class Transaction(models.Model):
    date = models.DateField(auto_now=True, null=False)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False)
    amount = models.DecimalField(decimal_places=2, blank=False, null=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.amount} - {self.comment}'

