from core.models import Notificacao
from home.views import BaseListView


class NotificacaoListView(BaseListView):
    model = Notificacao

    template_name = "core/notificacao/notificacao_list.html"

    title = "Notificações"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)
        context["create_title"] = "Adicionar notificação"

        return context

    def get_simple_fields_filter(self):
        """Função para definir os campos simples de filtro."""
        return [
            "id",
            "mensagem",
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
                crud_breadcrumbs.list_breadcrumb(Notificacao),
            ]
        )
