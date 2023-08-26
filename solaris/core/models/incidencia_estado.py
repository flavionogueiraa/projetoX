from django.db import models
from novadata_utils.models import NovadataModel


class IncidenciaEstado(NovadataModel):
    estado = models.CharField(
        verbose_name="Estado",
        max_length=100,
    )

    sigla = models.CharField(
        verbose_name="Sigla",
        max_length=2,
    )

    horas_sol_equivalentes = models.DecimalField(
        verbose_name="Horas de sol equivalentes",
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return f"{self.sigla} - {self.horas_sol_equivalentes}"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "core"
        verbose_name = "Incidência por estado"
        verbose_name_plural = "Incidências por estado"
