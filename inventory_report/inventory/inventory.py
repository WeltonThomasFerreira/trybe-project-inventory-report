import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if ".csv" in path:
            return cls.csv_reader(path, report_type)
        if ".json" in path:
            return cls.json_reader(path, report_type)
        if ".xml" in path:
            return cls.xml_reader(path, report_type)

    @classmethod
    def csv_reader(cls, path, report_type):
        data = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return cls.generate(data, report_type)

    @classmethod
    def json_reader(cls, path, report_type):
        with open(path) as file:
            data = json.load(file)
        return cls.generate(data, report_type)

    @classmethod
    def xml_reader(cls, path, report_type):
        with open(path) as file:
            reader = file.read()
            data = xmltodict.parse(reader)
            data = data['dataset']['record']
        return cls.generate(data, report_type)

    @classmethod
    def generate(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
