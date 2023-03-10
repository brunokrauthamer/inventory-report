import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory:
    @classmethod
    def import_data(cls, path, type):
        with open(path) as data_file:
            data_list = csv.DictReader(data_file)
            data = []
            for d in data_list:
                data.append(d)
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)