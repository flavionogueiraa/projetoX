from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from ...forms import PessoaForm
from ...models import Pessoa


class PessoaCreateView(LoginRequiredMixin, CreateView):
    model = Pessoa

    form_class = PessoaForm

    template_name = "core/pessoa/pessoa_form.html"

    def get_success_url(self):
        """Define a url de sucesso."""
        from django.urls import reverse_lazy

        return reverse_lazy("pessoa_list_view")

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)

        return context
