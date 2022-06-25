from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, importer, data):
        self.importer = importer
        self.data = data

    def __next__(self):
        data = self.importer.import_data(self.data)
        if not data:
            raise StopIteration()
        return data[0]
