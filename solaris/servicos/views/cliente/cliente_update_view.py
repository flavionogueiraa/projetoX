from core.forms import EnderecoForm
from django.views.generic.edit import UpdateView
from home.views import BaseNovadataView
from servicos.forms import ClienteForm, EstacaoSolarForm
from servicos.functions import salvar_endereco, salvar_estacao_solar
from servicos.models import Cliente


class ClienteUpdateView(BaseNovadataView, UpdateView):
    model = Cliente

    form_class = ClienteForm

    template_name = "servicos/cliente/cliente_form/cliente_form.html"

    title = "Editar cliente"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)

        has_endereco = hasattr(self.object, "endereco")
        endereco = self.object.endereco if has_endereco else None
        context["endereco_form"] = EnderecoForm(instance=endereco)

        estacao_solar = self.get_object().estacaosolar_set.first()
        if estacao_solar:
            context["estacao_solar_form"] = EstacaoSolarForm(
                instance=estacao_solar
            )
        else:
            context["estacao_solar_form"] = EstacaoSolarForm(
                initial={
                    "cliente": self.get_object().pk,
                },
            )

        return context

    def get_breadcrumb(self):
        """Função para definir os breadcrumbs."""
        from global_functions.breadcrumb import (
            crud_breadcrumbs,
            make_breadcrumb,
        )
        from global_functions.breadcrumb.itens import servicos

        return make_breadcrumb(
            [
                servicos,
                crud_breadcrumbs.list_breadcrumb(Cliente),
                crud_breadcrumbs.detail_breadcrumb(
                    Cliente, url_params=[self.object.pk]
                ),
                crud_breadcrumbs.update_breadcrumb(
                    Cliente, url_params=[self.object.pk]
                ),
            ]
        )

    def form_valid(self, form):
        """Implementações extras depois que o form é validado."""
        default_return = super().form_valid(form)
        salvar_endereco(self)
        salvar_estacao_solar(self)

        return default_return
