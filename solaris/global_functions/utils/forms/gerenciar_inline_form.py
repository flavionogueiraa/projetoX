from django.db import IntegrityError


def gerenciar_inline_form(inline_form):
    for form in inline_form:
        try:
            is_valid = form.is_valid()
            delete = form.cleaned_data.get("DELETE", False)

            if is_valid and not delete:
                form.save(commit=False)
                form.save()
            elif delete:
                try:
                    if form.instance.id:
                        form.instance.delete()
                except IntegrityError:
                    print("Não é possível deletar")
            else:
                print("Não é possível salvar, form inválido")
        except IntegrityError:
            pass
