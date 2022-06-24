import csv

from reports.complete_report import CompleteReport, SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        data = []

        if ".csv" in path:
            with open(path, newline="") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
                for row in reader:
                    data.append(row)
        return cls.generate(data, report_type)

    @classmethod
    def generate(cls, data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)
