from django.views.generic.edit import DeleteView
from home.views import BaseNovadataView
from servicos.models import Visita


class VisitaDeleteView(BaseNovadataView, DeleteView):
    model = Visita

    template_name = "servicos/visita/visita_delete.html"

    title = "Excluir visita"

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
                    Visita, url_params=[self.object.pk]
                ),
                crud_breadcrumbs.delete_breadcrumb(
                    Visita, url_params=[self.object.pk]
                ),
            ]
        )
