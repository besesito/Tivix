from budgets.views import (
    BudgetCreateView,
    BudgetDeleteView,
    BudgetListCreateView,
    BudgetListDeleteView,
    BudgetListUpdateView,
    BudgetUpdateView,
)
from django.urls import path

app_name = "budgets"

urlpatterns = [
    path("list/create", BudgetListCreateView.as_view(), name="create_list"),
    path("list/update/<str:pk>", BudgetListUpdateView.as_view(), name="update_list"),
    path("list/delete/<str:pk>", BudgetListDeleteView.as_view(), name="delete_list"),
    path(
        "budget/create/<str:list_id>", BudgetCreateView.as_view(), name="create_budget"
    ),
    path("budget/update/<str:pk>", BudgetUpdateView.as_view(), name="update_budget"),
    path("budget/delete/<str:pk>", BudgetDeleteView.as_view(), name="delete_budget"),
]
