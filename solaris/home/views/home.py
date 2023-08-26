from datetime import datetime, timedelta

from django.db.models import Count
from django.views.generic import TemplateView
from servicos.models import Cliente, EstacaoSolar, Funcionario, Visita

from .base_novadata_view import BaseNovadataView


class HomeView(BaseNovadataView, TemplateView):
    template_name = "home/home_page/home.html"

    need_title = False

    def get_breadcrumb(self):
        """Função para definir os breadcrumbs."""
        return []

    def get_context_data(self, **kwargs):
        """Informa o contexto que será passado para o template."""
        context = super().get_context_data(**kwargs)

        context["clientes"] = Cliente.objects.all()
        context["clientes_por_cidade"] = list(
            Cliente.objects.values("endereco__cidade")
            .distinct()
            .annotate(total=Count("id"))
            .order_by("?")
        )

        context["visitas"] = Visita.objects.all()
        context["visitas_por_cidade"] = list(
            Visita.objects.values("cliente__endereco__cidade")
            .distinct()
            .annotate(total=Count("id"))
            .order_by("?")
        )
        today = datetime.today()
        in_7days = today + timedelta(days=7)
        context["visits_on_next_7days"] = Visita.objects.filter(
            data_hora__gte=today,
            data_hora__lte=in_7days,
        ).order_by("data_hora")

        context["funcionarios_por_visita"] = list(
            Funcionario.objects.filter(visita__isnull=False)
            .values("nome")
            .distinct()
            .annotate(total_visitas=Count("visita"))
            .order_by("?")
        )

        context["estacoes"] = EstacaoSolar.objects.all()
        context["estacoes_por_kw_mensal"] = list(
            EstacaoSolar.objects.values("geracao_mensal", "cliente__nome")
            .distinct()
            .order_by("?")
        )

        return context
