import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if ".csv" in path:
            return cls.csv_reader(path, report_type)

    @classmethod
    def csv_reader(cls, path, report_type):
        data = []
        with open(path, newline="") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in reader:
                data.append(row)
        return cls.generate(data, report_type)

    @classmethod
    def generate(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        elif report_type == "completo":
            return CompleteReport.generate(data)
