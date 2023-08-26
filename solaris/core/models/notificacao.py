from django.contrib.auth.models import User
from django.db import models
from novadata_utils.models import NovadataModel


class Notificacao(NovadataModel):
    mensagem = models.CharField(
        verbose_name="Mensagem",
        max_length=100,
    )

    usuario = models.ForeignKey(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.mensagem

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "core"
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"
