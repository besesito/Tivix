from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from budgets.models import BudgetList


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            active_home="active",
            budgets=BudgetList.objects.user_list(self.request.user)
        )
        return context
