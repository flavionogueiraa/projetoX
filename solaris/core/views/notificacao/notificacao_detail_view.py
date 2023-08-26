from core.models import Notificacao
from django.views.generic.detail import DetailView
from home.views import BaseNovadataView


class NotificacaoDetailView(BaseNovadataView, DetailView):
    model = Notificacao

    template_name = "core/notificacao/notificacao_detail.html"

    title = "Detalhes da notificação"

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
                crud_breadcrumbs.detail_breadcrumb(
                    Notificacao,
                    url_params=[self.kwargs.get("pk")],
                ),
            ]
        )
