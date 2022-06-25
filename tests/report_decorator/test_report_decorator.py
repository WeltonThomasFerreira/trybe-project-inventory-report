from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport


mock = [
    {
        "id": 1,
        "nome_do_produto": "Cafe",
        "nome_da_empresa": "Cafes Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "instrucao",
    }
]


def test_decorar_relatorio():
    sut = ColoredReport(CompleteReport)
    report = sut.generate(mock)

    assert r"^\\033\[36mm.*\\033\[0m$".find(report)
    assert r"^\\033\[32mm.*\\033\[0m$".find(report)
    assert r"^\\033\[31mm.*\\033\[0m$".find(report)
    assert "\033[36m2023-02-09\033[0m" in report
