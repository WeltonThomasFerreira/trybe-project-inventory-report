from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report =  super().generate(data)
        complete_report = {}
        str_complete_report = ''
        companies = list(map(lambda company: company['nome_da_empresa'], data))

        for company in set(companies):
            complete_report[company] = companies.count(company)

        complete_report = sorted(complete_report.items(), key=lambda x: x[1], reverse=True)

        for company in complete_report:
            str_complete_report += f'- {company[0]}: {company[1]}\n'

        return (
            simple_report + 
            f'\nProdutos estocados por empresa:\n' +
            str_complete_report
        )
