from django.views.generic.edit import DeleteView
from home.views import BaseNovadataView
from servicos.models import Cliente


class ClienteDeleteView(BaseNovadataView, DeleteView):
    model = Cliente

    template_name = "servicos/cliente/cliente_delete.html"

    title = "Excluir cliente"

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
                crud_breadcrumbs.list_breadcrumb(Cliente),
                crud_breadcrumbs.detail_breadcrumb(
                    Cliente, url_params=[self.object.pk]
                ),
                crud_breadcrumbs.delete_breadcrumb(
                    Cliente, url_params=[self.object.pk]
                ),
            ]
        )
