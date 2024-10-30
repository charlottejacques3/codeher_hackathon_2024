from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=400)
    allowed_budget = models.IntegerField()

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=400)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return self.name
