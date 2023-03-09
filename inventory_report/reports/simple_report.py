from datetime import datetime

class SimpleReport:
    @classmethod
    def generate(cls, list):
        current_date = datetime.today().strftime('%Y-%m-%d')
        fabrication_dates = []
        expiration_dates = []
        companies = []
        for item in list:
            fabrication_dates.append(item['data_de_fabricacao'])
            companies.append(item['nome_da_empresa'])
            if item['data_de_validade'] >= current_date:
                expiration_dates.append(item['data_de_validade'])


        fabrication_dates.sort()
        expiration_dates.sort()

        oldest_fabrication_date = fabrication_dates[0]
        closest_expiration_date = expiration_dates[0]
        more_products_company = ''
        number_of_products = 0

        print(f'')

        for company in companies:
            count = companies.count(company)
            if count > number_of_products:
                number_of_products = count
                more_products_company = company
        
        return f"""Data de fabricação mais antiga: {oldest_fabrication_date}
Data de validade mais próxima: {closest_expiration_date}
Empresa com mais produtos: {more_products_company}"""


