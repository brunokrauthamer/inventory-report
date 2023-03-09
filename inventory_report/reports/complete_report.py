from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = SimpleReport.generate(list)
        sotkced_products_number = {}
        for product in list:
            try:
                sotkced_products_number[product['nome_da_empresa']]
            except KeyError:
                sotkced_products_number[product['nome_da_empresa']] = 1
            else:
                sotkced_products_number[product['nome_da_empresa']] += 1
        stocked_products_report = 'Produtos estocados por empresa:'
        for key in sotkced_products_number:
            stocked_products_report = f"""{stocked_products_report}
- {key}: {sotkced_products_number[key]}"""
        return f"""{simple_report}
{stocked_products_report}
"""
