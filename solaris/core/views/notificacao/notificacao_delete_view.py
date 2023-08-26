from core.models import Notificacao
from django.views.generic.edit import DeleteView
from home.views import BaseNovadataView


class NotificacaoDeleteView(BaseNovadataView, DeleteView):
    model = Notificacao

    template_name = "core/notificacao/notificacao_delete.html"

    title = "Excluir notificação"

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
                    Notificacao, url_params=[self.object.pk]
                ),
                crud_breadcrumbs.delete_breadcrumb(
                    Notificacao, url_params=[self.object.pk]
                ),
            ]
        )
