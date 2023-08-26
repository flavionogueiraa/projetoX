from core.forms import FornecedorForm
from core.models import Fornecedor
from django.views.generic.edit import UpdateView
from home.views import BaseNovadataView


class FornecedorUpdateView(BaseNovadataView, UpdateView):
    model = Fornecedor

    form_class = FornecedorForm

    template_name = "core/fornecedor/fornecedor_form.html"

    title = "Editar fornecedor"

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
                crud_breadcrumbs.list_breadcrumb(Fornecedor),
                crud_breadcrumbs.detail_breadcrumb(
                    Fornecedor, url_params=[self.object.pk]
                ),
                crud_breadcrumbs.update_breadcrumb(
                    Fornecedor, url_params=[self.object.pk]
                ),
            ]
        )
