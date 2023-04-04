from inventory_report.inventory.product import Product


def test_cria_produto():
    mockProduct = Product(
        1,
        "produto1",
        "Empresa1",
        "01/01/2023",
        "01/05/2023",
        "21a151FG",
        "Local seco",
    )

    assert mockProduct.id == 1
    assert mockProduct.nome_do_produto == "produto1"
    assert mockProduct.nome_da_empresa == "Empresa1"
    assert mockProduct.data_de_fabricacao == "01/01/2023"
    assert mockProduct.data_de_validade == "01/05/2023"
    assert mockProduct.numero_de_serie == "21a151FG"
    assert mockProduct.instrucoes_de_armazenamento == "Local seco"
