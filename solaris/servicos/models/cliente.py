from core.models import Pessoa
from django.db import models


class Cliente(Pessoa):
    termo_compromisso = models.FileField(
        verbose_name="Termo de compromisso",
        upload_to="termos_compromisso",
        null=True,
        blank=True,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "servicos"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
