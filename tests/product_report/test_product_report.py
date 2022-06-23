from inventory_report.inventory.product import Product


def test_relatorio_produto():
    sut = Product(
        1,
        "Farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "666172696E6861",
        "ao abrigo de luz",
    )

    report = sut.__repr__()

    assert report == (
        "O produto Farinha"
        " fabricado em 01-05-2021"
        " por Farinini com validade"
        " até 02-06-2023"
        " precisa ser armazenado ao abrigo de luz."
    )
