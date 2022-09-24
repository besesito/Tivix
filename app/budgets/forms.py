from django import forms
from django.contrib.auth.models import User

from budgets.models import BudgetList


class BudgetListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["shared_users"] = forms.ModelMultipleChoiceField(
            queryset=User.objects.exclude(id=self.author.id),
            required=False
        )

    def save(self, commit=True):
        self.instance.author = self.author
        return super().save(commit)

    class Meta:
        model = BudgetList
        fields = [
            "name",
            "shared_users"
        ]
