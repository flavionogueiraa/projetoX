from django.views.generic.detail import DetailView
from home.views import BaseNovadataView
from servicos.models import Funcionario


class FuncionarioDetailView(BaseNovadataView, DetailView):
    model = Funcionario

    template_name = "servicos/funcionario/funcionario_detail.html"

    title = "Detalhes da funcionário"

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
                crud_breadcrumbs.list_breadcrumb(Funcionario),
                crud_breadcrumbs.detail_breadcrumb(
                    Funcionario,
                    url_params=[self.kwargs.get("pk")],
                ),
            ]
        )
