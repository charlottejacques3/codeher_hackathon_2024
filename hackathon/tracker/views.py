from django.shortcuts import render
from django.urls import reverse_lazy
from django.template.defaulttags import register
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import *

# Create your views here.

class Home(TemplateView):
    template_name = 'tracker/homepage.html'

class Budget(TemplateView):
    template_name = 'tracker/budget.html'

    def get_spending_by_category(self) -> dict[int, int]:
        dict = {}
        categories = Category.objects.all()
        expenses = Expense.objects.all()
        for expense in expenses:
            if expense.category.id not in dict:
                dict[expense.category.id] = expense.amount
            else:
                dict[expense.category.id] += expense.amount
        return dict
    
    def categories_over(self):
        categories_over = []
        by_category = self.get_spending_by_category()
        for category_id in by_category:
            category = Category.objects.get(id=category_id)
            if by_category[category_id] > category.allowed_budget:
                categories_over.append(category.name)
        return categories_over

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'categories': Category.objects.all(),
            'by_category': self.get_spending_by_category(),
            'categories_over': self.categories_over()
        }
        return context

class Expenses(TemplateView):
    template_name = 'tracker/expenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            'expenses': Expense.objects.all().order_by('-date'),
        }
        return context
    
    
class CreateExpense(CreateView):
    model = Expense
    fields = ['name', 'date', 'category', 'amount']

    def get_success_url(self) -> str:
        return reverse_lazy('expenses')

class CreateCategory(CreateView):
    model = Category
    fields = ['name', 'allowed_budget']

    def get_success_url(self) -> str:
        return reverse_lazy('budget')
    


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)