from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from ...models import Pessoa


class PessoaDeleteView(LoginRequiredMixin, DeleteView):
    model = Pessoa

    template_name = "core/pessoa/pessoa_delete.html"

    def get_success_url(self):
        from django.urls import reverse_lazy

        return reverse_lazy("pessoa_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
