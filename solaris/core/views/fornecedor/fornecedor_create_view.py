from core.forms import FornecedorForm
from core.models import Fornecedor
from django.views.generic.edit import CreateView
from home.views import BaseNovadataView


class FornecedorCreateView(BaseNovadataView, CreateView):
    model = Fornecedor

    form_class = FornecedorForm

    template_name = "core/fornecedor/fornecedor_form.html"

    title = "Adicionar fornecedor"

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
                crud_breadcrumbs.create_breadcrumb(Fornecedor),
            ]
        )
