from core.forms import NotificacaoForm
from core.models import Notificacao
from django.views.generic.edit import CreateView
from home.views import BaseNovadataView


class NotificacaoCreateView(BaseNovadataView, CreateView):
    model = Notificacao

    form_class = NotificacaoForm

    template_name = "core/notificacao/notificacao_form.html"

    title = "Adicionar notificação"

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
                crud_breadcrumbs.create_breadcrumb(Notificacao),
            ]
        )
