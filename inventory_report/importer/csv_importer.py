from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path[-1] != 'v':
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as data_file:
                data_list = csv.DictReader(data_file)
                data = []
                for d in data_list:
                    data.append(d)
        return data
