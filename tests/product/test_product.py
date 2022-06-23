from inventory_report.inventory.product import Product


sut = Product(
    1,
    "Farinha",
    "Farinini",
    "01-05-2021",
    "02-06-2023",
    "666172696E6861",
    "ao abrigo de luz",
)


def test_cria_produto():
    assert type(sut) == Product
    assert type(sut.id) is int
    assert type(sut.nome_do_produto) is str
    assert type(sut.nome_da_empresa) is str
    assert type(sut.data_de_fabricacao) is str
    assert type(sut.data_de_validade) is str
    assert type(sut.numero_de_serie) is str
    assert type(sut.instrucoes_de_armazenamento) is str
