from django.db import models
from novadata_utils.models import NovadataModel

from .cliente import Cliente


class EstacaoSolar(NovadataModel):
    cliente = models.ForeignKey(
        Cliente,
        verbose_name="Cliente",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    quantidade_placas = models.IntegerField(
        verbose_name="Quantidade de placas necessárias",
    )

    consumo_mensal = models.DecimalField(
        verbose_name="Consumo mensal (kW/h)",
        max_digits=10,
        decimal_places=2,
    )

    geracao_mensal = models.DecimalField(
        verbose_name="Geração mensal por placa (kW/h)",
        max_digits=10,
        decimal_places=2,
    )

    kw_placa = models.DecimalField(
        verbose_name="(kW/h) da placa",
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    valor_cada_placa = models.DecimalField(
        verbose_name="Valor de cada placa",
        max_digits=10,
        decimal_places=2,
        null=True,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return "Estação solar de {}".format(self.cliente)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "servicos"
        verbose_name = "Estação solar"
        verbose_name_plural = "Estações solares"
