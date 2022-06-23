from statistics import mode

class SimpleReport:
    @classmethod
    def generate(cls, data):
        oldest_date = min(map(lambda x: x['data_de_fabricacao'], data))
        closest_date = min(map(lambda x: x['data_de_validade'], data))
        list_company_names = list(map(lambda x: x['nome_da_empresa'], data))
        company_bigger_stock = mode(list_company_names)

        return (
            f'Data de fabricação mais antiga: {oldest_date}\n'
            f'Data de validade mais próxima: {closest_date}\n'
            f'Empresa com mais produtos: {company_bigger_stock}'
        )