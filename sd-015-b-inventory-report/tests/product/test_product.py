from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = "salgadinho"
    nome_da_empresa = "Swift"
    data_de_fabricacao = "05/07/2022"
    data_de_validade = "15/07/2022"
    numero_de_serie = "123456"
    instrucoes_de_armazenamento = "manter congelado"
    produto = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert produto.id == id
    assert produto.nome_do_produto == nome_do_produto
    assert produto.nome_da_empresa == nome_da_empresa
    assert produto.data_de_fabricacao == data_de_fabricacao
    assert produto.data_de_validade == data_de_validade
    assert produto.numero_de_serie == numero_de_serie
    assert produto.instrucoes_de_armazenamento == instrucoes_de_armazenamento
