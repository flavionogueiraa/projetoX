from django.contrib.auth import login
from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestUser(TestCase):
    def setUp(self):
        """Implementa algumas ações antes de iniciar cada teste."""
        self.cliennt = Client()
        self.usuario = User.objects.create(
            username="usuario",
            email="email@example.com",
            password="password-example",
        )

    def test_login(self):
        """Testa o login."""
        self.client.login(
            username=self.usuario.email,
            password=self.usuario.password,
        )
        self.assertTrue(self.usuario.is_authenticated)


# Não funcionais:
# [RNF001] Atividade de login
# O sistema de guardar a atividade de login dos usuários pela última vez de uso
# Ok, temos uns campos no admin para isso, podemos só tirar alguns prints.

# [RNF002] Logs do usuário
# O sistema deve registrar os logs do usuário.
# Ok, temos menus no admin para isso, podemos só tirar alguns prints.

# RNF005] Quantidade de usuário conectados
# O sistema deve suportar um número máximo de 100 usuários conectados simultaneamente.  # noqa E501
# Talvez até consigamos logar 100 usuários, mas teremos que limitar o
# número máximo para 100? Meio estranho, não acham?
