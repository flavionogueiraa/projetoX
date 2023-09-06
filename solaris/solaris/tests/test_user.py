from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestUser(TestCase):
    USERS_EXPECTED = 100

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

    def test_quantity_connected_users(self):
        """Testa a quantidade de usuários conectados."""
        for i in range(self.USERS_EXPECTED):
            username = f"usuario{i}"
            email = f"email{i}@example.com"
            password = f"password-example{i}"

            User.objects.create(
                username=username,
                email=email,
                password=password,
            )
            self.client.login(
                username=email,
                password=password,
            )
            self.assertTrue(self.usuario.is_authenticated)
