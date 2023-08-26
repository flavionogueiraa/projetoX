from django.views.generic.edit import UpdateView
from home.views import BaseNovadataView
from servicos.forms import VisitaForm
from servicos.models import Visita


class VisitaUpdateView(BaseNovadataView, UpdateView):
    model = Visita

    form_class = VisitaForm

    template_name = "servicos/visita/visita_form.html"

    title = "Editar visita"

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
                crud_breadcrumbs.update_breadcrumb(
                    Visita, url_params=[self.object.pk]
                ),
            ]
        )
