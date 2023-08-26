from core.models import Pessoa
from django.contrib.auth.models import User
from django.db import models


class Funcionario(Pessoa):
    usuario = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "servicos"
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
