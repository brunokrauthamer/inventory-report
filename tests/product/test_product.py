from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = 'nome_do_produto'
    nome_da_empresa = 'nome_da_empresa'
    data_de_fabricacao = 'data_de_fabricacao'
    data_de_validade = 'data_de_validade'
    numero_de_serie = 1
    instrucoes_de_armazenamento = 'instrucoes_de_armazenamento'
    product = Product(id, nome_do_produto, nome_da_empresa, data_de_fabricacao, data_de_validade, numero_de_serie, instrucoes_de_armazenamento)
    print(product)
    assert product.id == 1
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == 1
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento

