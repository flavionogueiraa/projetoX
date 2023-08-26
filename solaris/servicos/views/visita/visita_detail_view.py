from django.views.generic.detail import DetailView
from home.views import BaseNovadataView
from servicos.models import Visita


class VisitaDetailView(BaseNovadataView, DetailView):
    model = Visita

    template_name = "servicos/visita/visita_detail.html"

    title = "Detalhes da visita"

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
                crud_breadcrumbs.list_breadcrumb(Visita),
                crud_breadcrumbs.detail_breadcrumb(
                    Visita,
                    url_params=[self.kwargs.get("pk")],
                ),
            ]
        )
