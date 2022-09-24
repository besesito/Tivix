from budgets.models import Budget, BudgetList
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class BudgetListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["shared_users"] = forms.ModelMultipleChoiceField(
            queryset=User.objects.exclude(id=self.author.id), required=False
        )

    def save(self, commit=True):
        self.instance.author = self.author
        return super().save(commit)

    class Meta:
        model = BudgetList
        fields = ["name", "shared_users"]


class BudgetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("user")
        self.list_id = kwargs.pop("list_id")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.budget_list = get_object_or_404(BudgetList, id=self.list_id)
        self.instance.author = self.author
        return super().save(commit)

    class Meta:
        model = Budget
        fields = [
            "name",
            "kind",
            "amount",
        ]
