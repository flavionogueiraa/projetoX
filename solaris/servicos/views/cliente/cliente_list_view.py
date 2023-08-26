from home.views import BaseListView
from servicos.models import Cliente


class ClienteListView(BaseListView):
    model = Cliente

    template_name = "servicos/cliente/cliente_list.html"

    title = "Clientes"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)
        context["create_title"] = "Adicionar cliente"

        return context

    def get_simple_fields_filter(self):
        """Função para definir os campos simples de filtro."""
        return [
            "id",
            "nome",
            "email",
            "telefone",
            "cpf_cnpj",
        ]

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
            ]
        )
