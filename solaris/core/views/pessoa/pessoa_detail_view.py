from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from ...models import Pessoa


class PessoaDetailView(LoginRequiredMixin, DetailView):
    model = Pessoa

    template_name = "core/pessoa/pessoa_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
