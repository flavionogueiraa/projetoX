from core.models import Notificacao
from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin


@admin.register(Notificacao)
class NotificacaoAdmin(NovadataModelAdmin):
    ...
