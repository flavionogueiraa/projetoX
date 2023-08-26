from django.db import models
from novadata_utils.models import NovadataModel


class Pessoa(NovadataModel):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    email = models.EmailField(
        verbose_name="E-mail",
        max_length=100,
    )

    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=20,
    )

    cpf_cnpj = models.CharField(
        verbose_name="CPF",
        max_length=30,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "core"
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
