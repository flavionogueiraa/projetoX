from core.models import Pessoa
from home.views import BaseListView


class PessoaListView(BaseListView):
    model = Pessoa

    template_name = "core/pessoa/pessoa_list.html"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Pessoas"
        context["create_title"] = "Nova pessoa"

        return context

    def get_simple_fields_filter(self):
        """Função para definir os campos simples de filtro."""
        return [
            "id",
            "nome",
            "email",
            "telefone",
            "cpf_cnpj",
            "usuario__username",
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
                crud_breadcrumbs.list_breadcrumb(
                    Pessoa,
                    "Pessoas",
                ),
            ]
        )
