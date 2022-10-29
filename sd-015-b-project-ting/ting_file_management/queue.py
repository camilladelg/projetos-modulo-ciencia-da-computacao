class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if not bool(self.__len__()):
            return None

        return self._data.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= self.__len__():
            raise IndexError("Indice inválido")

        return self._data[index]
