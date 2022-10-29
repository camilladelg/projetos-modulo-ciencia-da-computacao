from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "salgadinho"
    nome_da_empresa = "Swift"
    data_de_fabricacao = "05/07/2022"
    data_de_validade = "15/07/2022"
    numero_de_serie = "123456"
    instrucoes_de_armazenamento = "no congelador"
    produto = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    string = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa}"
        f" com validade até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )
    assert produto.__repr__() == string
