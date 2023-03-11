from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path[-1] != 'l':
            raise ValueError("Arquivo inválido")
        else:
            tree = ET.parse(path)
            root = tree.getroot()

            inventory_list = []

            for product in root:
                product_dict = {}
                for item in product:
                    product_dict[item.tag] = item.text
                inventory_list.append(product_dict)
        return inventory_list
