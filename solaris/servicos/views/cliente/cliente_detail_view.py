from django.views.generic.detail import DetailView
from home.views import BaseNovadataView
from servicos.models import Cliente, EstacaoSolar


class ClienteDetailView(BaseNovadataView, DetailView):
    model = Cliente

    template_name = "servicos/cliente/cliente_detail/cliente_detail.html"

    title = "Detalhes do(a) cliente"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)
        context["visitas"] = self.object.visita_set.all().order_by("data_hora")
        context['estacao_solar'] = EstacaoSolar.objects.filter(
            cliente = self.get_object()
        ).first()
        return context

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
                    Cliente,
                    url_params=[self.kwargs.get("pk")],
                ),
            ]
        )
