from core.models import Fornecedor
from home.views import BaseListView


class FornecedorListView(BaseListView):
    model = Fornecedor

    template_name = "core/fornecedor/fornecedor_list.html"

    title = "Fornecedores"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)
        context["create_title"] = "Adicionar fornecedor"

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
        from global_functions.breadcrumb.itens import core

        return make_breadcrumb(
            [
                core,
                crud_breadcrumbs.list_breadcrumb(Fornecedor),
            ]
        )
