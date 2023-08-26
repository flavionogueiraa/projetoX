from core.forms import NotificacaoForm
from core.models import Notificacao
from django.views.generic.edit import UpdateView
from home.views import BaseNovadataView


class NotificacaoUpdateView(BaseNovadataView, UpdateView):
    model = Notificacao

    form_class = NotificacaoForm

    template_name = "core/notificacao/notificacao_form.html"

    title = "Editar notificação"

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
                crud_breadcrumbs.update_breadcrumb(
                    Notificacao, url_params=[self.object.pk]
                ),
            ]
        )
