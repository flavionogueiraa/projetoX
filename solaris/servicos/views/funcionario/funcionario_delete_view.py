from django.views.generic.edit import DeleteView
from home.views import BaseNovadataView
from servicos.models import Funcionario


class FuncionarioDeleteView(BaseNovadataView, DeleteView):
    model = Funcionario

    template_name = "servicos/funcionario/funcionario_delete.html"

    title = "Excluir funcionário"

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
                    Funcionario, url_params=[self.object.pk]
                ),
                crud_breadcrumbs.delete_breadcrumb(
                    Funcionario, url_params=[self.object.pk]
                ),
            ]
        )
