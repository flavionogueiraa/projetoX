from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from ...forms import PessoaForm
from ...models import Pessoa


class PessoaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pessoa

    form_class = PessoaForm

    template_name = "core/pessoa/pessoa_form.html"

    def get_success_url(self):
        from django.urls import reverse_lazy

        return reverse_lazy(
            "pessoa_detail_view",
            kwargs={
                "pk": self.object.pk,
            },
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context
