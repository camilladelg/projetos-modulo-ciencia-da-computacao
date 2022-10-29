import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        listData = []
        if path.endswith("csv"):
            with open(path, encoding="utf-8") as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                for d in data:
                    listData.append(d)
                # print(listData)
        elif path.endswith("xml"):
            with open(path, encoding="utf-8") as file:
                data = xmltodict.parse(file.read())
                listData = data["dataset"]["record"]
        else:
            with open(path) as file:
                listData = json.load(file)

        # print(listData)
        if type == "simples":
            return SimpleReport.generate(listData)
        else:
            return CompleteReport.generate(listData)


# Inventory.import_data("inventory_report/data/inventory.xml", "simples")


# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
# referencia para leitura xml
