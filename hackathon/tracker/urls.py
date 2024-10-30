from django.urls import path
from . import views

urlpatterns = [
    path('budget/', views.Budget.as_view(), name='budget'),
    path('add-expense/', views.CreateExpense.as_view(), name='create_expense'),
    path('add-category/', views.CreateCategory.as_view(), name='create_category'),
    path('', views.Home.as_view(), name='home'),
    path('expenses/', views.Expenses.as_view(), name='expenses')
]