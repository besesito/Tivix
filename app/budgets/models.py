from django.contrib.auth.models import User
from django.db import models
from Tivix.models import CommonInfo


class BudgetListManager(models.Manager):
    def user_list(self, user):
        return self.get_queryset().prefetch_related("budgets").filter(author=user)

    def shared_list(self, user):
        return self.get_queryset().prefetch_related("budgets").filter(shared_users=user)


class BudgetList(CommonInfo):
    name = models.CharField(max_length=255)
    objects = BudgetListManager()
    shared_users = models.ManyToManyField(User, related_name="shared_lists", blank=True)

    def __str__(self):
        return self.name


class BudgetManager(models.Manager):
    def income(self, user):
        return self.get_queryset().filter(kind="income")

    def expense(self, user):
        return self.get_queryset().filter(kind="expense")


class Budget(CommonInfo):
    kinds = [
        ("in", "income"),
        ("ex", "expense")
    ]
    kind = models.CharField(max_length=255, choices=kinds)
    name = models.CharField(max_length=255)
    budget_list = models.ForeignKey(BudgetList, on_delete=models.CASCADE, related_name="budgets")
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=False)

    def __str__(self):
        return f"{self.name} - {self.amount}"
