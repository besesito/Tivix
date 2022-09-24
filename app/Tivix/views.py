from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from budgets.models import BudgetList


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.__dict__['environ'].get("HTTP_HX_REQUEST"):
            self.template_name = "partials/budget_lists.html"
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            active_home="active",
            my_lists=BudgetList.objects.user_list(self.request.user),
            shared_lists=BudgetList.objects.shared_list(self.request.user)
        )
        return context
