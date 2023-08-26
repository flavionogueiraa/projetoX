from core.models import Endereco
from django.contrib import admin


class EnderecoInline(admin.StackedInline):
    model = Endereco

    min = 1
