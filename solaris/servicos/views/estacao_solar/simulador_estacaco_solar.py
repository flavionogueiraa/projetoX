from django.views.generic import TemplateView
from home.views import BaseNovadataView
from servicos.forms import EstacaoSolarForm


class SimuladorEstacaoSolarView(BaseNovadataView, TemplateView):
    template_name = "servicos/estacao_solar/simulador_estacao_solar.html"

    title = "Simulador de estação"

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)

        context["estacao_solar_form"] = EstacaoSolarForm()

        return context

    def get_breadcrumb(self):
        """Função para definir os breadcrumbs."""
        from global_functions.breadcrumb import make_breadcrumb
        from global_functions.breadcrumb.itens import servicos

        simulador_estacaco = {
            "name": "Simulador de estação",
            "slug": "simulador_estacaco",
            "url_name": "simulador_estacao_solar_view",
        }

        return make_breadcrumb(
            [
                servicos,
                simulador_estacaco,
            ]
        )
