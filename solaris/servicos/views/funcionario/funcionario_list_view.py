from home.views import BaseListView
from servicos.models import Funcionario


class FuncionarioListView(BaseListView):
    model = Funcionario

    template_name = "servicos/funcionario/funcionario_list.html"

    title = "Funcionários"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)
        context["create_title"] = "Adicionar funcionário"

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
        from global_functions.breadcrumb.itens import servicos

        return make_breadcrumb(
            [
                servicos,
                crud_breadcrumbs.list_breadcrumb(Funcionario),
            ]
        )
