from django.urls import reverse_lazy
from django.views import generic

from budgets.forms import BudgetListForm
from budgets.models import BudgetList


class BudgetListCreateView(generic.CreateView):
    model = BudgetList
    template_name = "partials/form.html"
    form_class = BudgetListForm
    success_url = reverse_lazy("home")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Create",
            title="Create budget list",
        )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

