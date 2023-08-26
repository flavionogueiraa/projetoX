from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django_full_crud.utils import camel_to_snake_case
from novadata_utils.redirect import reverse_lazy_plus


class BaseNovadataView(LoginRequiredMixin, View):
    need_breadcrumb = True

    need_title = True

    title = ""

    def get_lower_model(self):
        """Função para retornar o nome do model em minúsculo."""
        has_model = hasattr(self, "model")
        if has_model and self.model:
            model_name = self.model.__name__
            return camel_to_snake_case(model_name)
        else:
            has_lower_model = hasattr(self, "lower_model")
            return self.lower_model if has_lower_model else ""

    def get_context_data(self, **kwargs):
        """Função para retornar o contexto da view."""
        context = super().get_context_data(**kwargs)
        context["breadcrumb"] = self.get_breadcrumb()
        context["lower_model"] = self.get_lower_model()
        context["title"] = self.get_title()

        return context

    def get_breadcrumb(self):
        """Função para definir os breadcrumbs."""
        if self.need_breadcrumb:
            name = self.__class__.__name__
            raise NotImplementedError(
                f"A classe {name} não implementou os breadcrumbs. Caso não seja necessário, sete a variável need_breadcrumb para False."  # noqa - E501
            )
        else:
            return []

    def get_title(self):
        """Função para retornar o título da página."""
        if self.need_title and not self.title:
            name = self.__class__.__name__
            raise NotImplementedError(
                f"A classe {name} não possui o título da página. Caso não seja necessário, sete a variável need_title para False."  # noqa - E501
            )
        else:
            return self.title

    def get_success_url(self):
        """Define a url de sucesso."""
        return reverse_lazy_plus(
            f"{self.get_lower_model()}_list_view",
            just_uri=True,
            get_params={
                "mensagem_toastify": "Operação realizada com sucesso!",
            },
        )
