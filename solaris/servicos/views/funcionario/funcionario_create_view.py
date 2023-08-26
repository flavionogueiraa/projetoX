from django.views.generic.edit import CreateView
from home.views import BaseNovadataView
from servicos.forms import FuncionarioForm
from servicos.models import Funcionario


class FuncionarioCreateView(BaseNovadataView, CreateView):
    model = Funcionario

    form_class = FuncionarioForm

    template_name = "servicos/funcionario/funcionario_form.html"

    title = "Adicionar funcionário"

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
                crud_breadcrumbs.create_breadcrumb(Funcionario),
            ]
        )
