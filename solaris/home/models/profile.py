from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    usuario = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return f"{self.usuario}"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "home"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
