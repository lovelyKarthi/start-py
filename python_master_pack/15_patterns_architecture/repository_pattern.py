"""Repository pattern example (thin wrapper over DB session)"""
class InMemoryRepo:
    def __init__(self):
        self._data = {}
    def add(self, id, item):
        self._data[id] = item
    def get(self, id):
        return self._data.get(id)
