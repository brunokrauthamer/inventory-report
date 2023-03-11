import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_xml(cls, path):
        tree = ET.parse(path)
        root = tree.getroot()

        inventory_list = []

        for product in root:
            product_dict = {}
            for item in product:
                product_dict[item.tag] = item.text
            inventory_list.append(product_dict)
        return inventory_list

    @classmethod
    def generate_report(cls, type, data):
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def import_data(cls, path, type):
        if path[-1] == 'l':
            data = cls.import_xml(path)
        elif path[-1] == 'v':
            with open(path) as data_file:
                data_list = csv.DictReader(data_file)
                data = []
                for d in data_list:
                    data.append(d)
        else:
            with open(path) as data_file:
                data_list = json.load(data_file)
                data = []
                for d in data_list:
                    data.append(d)
        return cls.generate_report(type, data)
