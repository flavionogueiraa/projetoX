from datetime import datetime

from django.db import models
from novadata_utils.models import NovadataModel

from .cliente import Cliente
from .funcionario import Funcionario


class Visita(NovadataModel):
    TIPO_CHOICES = [
        ("Manutenção", "Manutenção"),
        ("Instalação", "Instalação"),
        ("Proposta", "Proposta"),
        ("Chamado", "Chamado"),
    ]

    tipo = models.CharField(
        verbose_name="Tipo",
        max_length=100,
        choices=TIPO_CHOICES,
    )

    data_hora = models.DateTimeField(
        verbose_name="Data e hora",
    )

    funcionario = models.ForeignKey(
        Funcionario,
        verbose_name="Funcionário",
        on_delete=models.SET_NULL,
        null=True,
    )

    cliente = models.ForeignKey(
        Cliente,
        verbose_name="Cliente",
        on_delete=models.SET_NULL,
        null=True,
    )

    observacoes = models.TextField(
        verbose_name="Observações",
        blank=True,
        null=True,
    )

    realizada = models.BooleanField(
        verbose_name="Realizada",
        default=False,
    )

    @property
    def status(self):
        """Método que retorna o status da visita."""
        if self.realizada:
            return "Realizada"

        today = datetime.today()
        time_delta = today - self.data_hora
        faz_mais_de_2_dias = time_delta.days > 2

        if faz_mais_de_2_dias:
            return "Atrasada"

        return "Pendente"

    @property
    def status_class(self):
        """Método que retorna a classe do status da visita."""
        status_dict = {
            "Realizada": "bg-primary-blue",
            "Pendente": "bg-alert-warning-100",
            "Atrasada": "bg-alert-red-100",
        }

        return status_dict[self.status]

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        data_hora_formatada = self.data_hora.strftime("%d/%m/%Y %H:%M")
        return f"Visita a(o) cliente {self.cliente} - {data_hora_formatada}"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "servicos"
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
