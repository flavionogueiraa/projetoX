from django.db import models


class Endereco(models.Model):
    cep = models.CharField(
        verbose_name="CEP",
        max_length=9,
    )

    rua = models.CharField(
        verbose_name="Rua",
        max_length=100,
    )

    numero = models.CharField(
        verbose_name="Número",
        max_length=15,
    )

    bairro = models.CharField(
        verbose_name="Bairro",
        max_length=100,
    )

    referencia = models.CharField(
        verbose_name="Ponto de referência",
        max_length=100,
        blank=True,
        null=True,
    )

    cidade = models.CharField(
        verbose_name="Cidade",
        max_length=100,
        null=True,
    )

    estado = models.CharField(
        verbose_name="Estado",
        max_length=100,
        null=True,
    )

    latitude = models.CharField(
        verbose_name="Latitude",
        max_length=100,
        blank=True,
        null=True,
    )

    longitude = models.CharField(
        verbose_name="Longitude",
        max_length=100,
        blank=True,
        null=True,
    )

    cliente = models.OneToOneField(
        "servicos.Cliente",
        verbose_name="Cliente",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        if (
            self.cep
            and self.rua
            and self.numero
            and self.bairro
            and self.cidade
        ):
            return f"{self.cep} | {self.rua}, {self.numero}, {self.bairro} - {self.cidade}"  # noqa E501
        else:
            return "Favor completar o cadastro de endereço"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "core"
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
