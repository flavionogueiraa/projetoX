from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from servicos.models import Visita


@admin.register(Visita)
class VisitaAdmin(NovadataModelAdmin):
    ...
