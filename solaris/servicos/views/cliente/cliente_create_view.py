from core.forms import EnderecoForm
from django.views.generic.edit import CreateView
from home.views import BaseNovadataView
from servicos.forms import ClienteForm, EstacaoSolarForm
from servicos.functions import salvar_endereco, salvar_estacao_solar
from servicos.models import Cliente


class ClienteCreateView(BaseNovadataView, CreateView):
    model = Cliente

    form_class = ClienteForm

    template_name = "servicos/cliente/cliente_form/cliente_form.html"

    title = "Adicionar cliente"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)

        context["endereco_form"] = EnderecoForm()
        context["estacao_solar_form"] = EstacaoSolarForm()

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
                crud_breadcrumbs.create_breadcrumb(Cliente),
            ]
        )

    def form_valid(self, form):
        """Implementações extras depois que o form é validado."""
        default_return = super().form_valid(form)
        salvar_endereco(self)
        salvar_estacao_solar(self)

        return default_return
