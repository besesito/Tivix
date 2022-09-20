from django.urls import path
from budgets.views import BudgetListCreateView

app_name = "budgets"

urlpatterns = [
    path('list/create', BudgetListCreateView.as_view(), name='create_list'),
]
