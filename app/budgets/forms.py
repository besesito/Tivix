from django import forms

from budgets.models import BudgetList


class BudgetListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.author = self.author
        return super().save(commit)

    class Meta:
        model = BudgetList
        fields = [
            "name",
            "shared_users"
        ]
