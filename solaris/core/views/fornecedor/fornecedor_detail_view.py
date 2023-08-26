from core.models import Fornecedor
from django.views.generic.detail import DetailView
from home.views import BaseNovadataView


class FornecedorDetailView(BaseNovadataView, DetailView):
    model = Fornecedor

    template_name = "core/fornecedor/fornecedor_detail.html"

    title = "Detalhes da fornecedor"

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
                    Fornecedor,
                    url_params=[self.kwargs.get("pk")],
                ),
            ]
        )
