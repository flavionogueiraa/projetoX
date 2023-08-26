from django.db.models import Q


def filter_by_text(query, simple_fields: list, booleans: tuple, value: str):
    """
    Função para fazermos filtros guiados pelo backend em tabelas.

    Parecido com aquela coisa que o datatable faz,passa por todos
    os campos verificando se o valor é igual ao que o usuário digitou.

    Parâmetros:
        query: QuerySet a ser filtrado | Formato esperado: <QuerySet []>.
        simple_fields: Lista de campos simples que podem ser filtrados | Formato esperado: ['nome_normal', 'campo_fk__nome'].
        booleans: Lista de campos booleans que podem ser filtrados | Formato esperado: [('campo', ['Valor verdadeiro na tabela', 'Valor falso na tabela'])].
        value: Valor a ser filtrado | Formato esperado: 'String normal'.
    """

    expression = Q()
    for field in simple_fields:
        expression = expression | Q((f"{field}__icontains", value))

    if check_rigth_format_booleans(booleans):
        tuple_booleans = map(make_tuple_of_boolean, booleans)
        for boolean in tuple_booleans:
            expression = expression | Q(
                (f"{boolean.field}", compare_values(boolean.values, value))
            )

    query = query.filter(expression)
    return query


def check_rigth_format_booleans(booleans):
    def check_boolean(boolean):
        if boolean[0] and boolean[0][0] and boolean[0][1]:
            return True
        else:
            return False

    if booleans:
        if len(list(filter(check_boolean, booleans))) == len(booleans):
            return True
    return False


def make_tuple_of_boolean(boolean):
    from collections import namedtuple

    if len(boolean) == 2:
        BooleanField = namedtuple("BooleanField", ["field", "values"])
        return BooleanField(boolean[0], boolean[1])
    else:
        print(
            "Erro em make_tuple_of_boolean, é esperado um valor no formato (field, [valor_true, valor_false])"
        )
        return None


def compare_values(values, value):
    if values[0] == value:
        return True
    elif values[1] == value:
        return False

    return None
