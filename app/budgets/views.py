from budgets.forms import BudgetForm, BudgetListForm
from budgets.models import Budget, BudgetList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views import generic


class BudgetListCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = BudgetList
    template_name = "partials/form_htmx.html"
    form_class = BudgetListForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Create",
            title="Create budget list",
            url=reverse_lazy("budgets:create_list"),
            modal=True,
        )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def get_success_message(self, cleaned_data):
        return f"Created new budget list - {cleaned_data['name']}"


class BudgetListUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = BudgetList
    template_name = "partials/form_htmx.html"
    form_class = BudgetListForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Update",
            title="Update budget list",
            url=reverse("budgets:update_list", args=[self.kwargs["pk"]]),
            modal=True,
        )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def get_success_message(self, cleaned_data):
        return f"Updated budget list - {cleaned_data['name']}"


class BudgetListDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = BudgetList
    template_name = "partials/form_htmx.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Delete",
            title=f"Do You want to delete {self.object}",
            url=reverse("budgets:delete_list", args=[self.kwargs["pk"]]),
            modal=True,
        )
        return context

    def get_success_message(self, cleaned_data):
        return f"Deleted budget list - {self.object.name}"


class BudgetCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Budget
    template_name = "partials/form_htmx.html"
    form_class = BudgetForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Create",
            title="Create budget",
            url=reverse("budgets:create_budget", args=[self.kwargs["list_id"]]),
            modal=True,
        )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        kwargs.update({"list_id": self.kwargs["list_id"]})
        return kwargs

    def get_success_message(self, cleaned_data):
        return f"Created new budget - {cleaned_data['name']}"


class BudgetUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Budget
    template_name = "partials/form_htmx.html"
    fields = [
        "name",
        "kind",
        "amount",
    ]
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Update",
            title="Update budget",
            url=reverse("budgets:update_budget", args=[self.kwargs["pk"]]),
            modal=True,
        )
        return context

    def get_success_message(self, cleaned_data):
        return f"Updated budget - {cleaned_data['name']}"


class BudgetDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Budget
    template_name = "partials/form_htmx.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            method="post",
            value_button="Delete",
            title=f"Do You want to delete {self.object}",
            url=reverse("budgets:delete_budget", args=[self.kwargs["pk"]]),
            modal=True,
        )
        return context

    def get_success_message(self, cleaned_data):
        return f"Deleted budget - {self.object.name}"
