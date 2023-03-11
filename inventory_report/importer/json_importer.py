from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path[-1] != 'n':
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as data_file:
                data_list = json.load(data_file)
                data = []
                for d in data_list:
                    data.append(d)
        return data
