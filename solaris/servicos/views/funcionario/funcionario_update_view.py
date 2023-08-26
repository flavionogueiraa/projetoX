from django.views.generic.edit import UpdateView
from home.views import BaseNovadataView
from servicos.forms import FuncionarioForm
from servicos.models import Funcionario


class FuncionarioUpdateView(BaseNovadataView, UpdateView):
    model = Funcionario

    form_class = FuncionarioForm

    template_name = "servicos/funcionario/funcionario_form.html"

    title = "Editar funcionário"

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
                crud_breadcrumbs.update_breadcrumb(
                    Funcionario, url_params=[self.object.pk]
                ),
            ]
        )
