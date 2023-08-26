from core.models import Fornecedor
from django.views.generic.edit import DeleteView
from home.views import BaseNovadataView


class FornecedorDeleteView(BaseNovadataView, DeleteView):
    model = Fornecedor

    template_name = "core/fornecedor/fornecedor_delete.html"

    title = "Excluir fornecedor"

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
                crud_breadcrumbs.delete_breadcrumb(
                    Fornecedor, url_params=[self.object.pk]
                ),
            ]
        )
