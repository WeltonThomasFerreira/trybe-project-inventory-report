from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        str_complete_report = ""
        companies = list(map(lambda company: company["nome_da_empresa"], data))

        for company in list(dict.fromkeys(companies)):
            str_complete_report += f"- {company}: {companies.count(company)}\n"

        return (
            simple_report
            + "\nProdutos estocados por empresa:\n"
            + str_complete_report
        )
