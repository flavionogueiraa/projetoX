from django.http import JsonResponse
from django.views.generic.list import ListView
from global_functions.filters.table_filters import filter_by_text, ordenar_th

from .base_novadata_view import BaseNovadataView


class BaseListView(BaseNovadataView, ListView):
    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get("paginate_by", 10)
        return paginate_by

    def get(self, request, *args, **kwargs):
        default_return = super().get(request, *args, **kwargs)
        get_totalizadores = request.GET.get("totalizadores", False)
        if get_totalizadores:
            return JsonResponse(self.get_totalizadores())
        return default_return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "")
        context["order"] = self.request.GET.get("order", "")
        context["columns"] = self.get_columns()

        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()

        filter = self.request.GET.get("filter", None)
        order = self.request.GET.get("order", None)

        if filter:
            simple_fields = self.get_simple_fields_filter()
            boolean_fields = self.get_booleans_fields_filter()

            queryset = filter_by_text(
                queryset, simple_fields, boolean_fields, filter
            )

        if order:
            queryset = ordenar_th(order, queryset)

        return queryset

    def get_simple_fields_filter(self):
        return []

    def get_booleans_fields_filter(self):
        # [("campo", ["Valor verdadeiro na tabela", "Valor falso na tabela"])]
        return [("", ["", ""])]

    def get_columns(self):
        return {}

    def get_totalizadores(self):
        return {}
