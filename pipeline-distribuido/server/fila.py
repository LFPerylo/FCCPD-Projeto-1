from queue import Queue

class FilaLimitada:
    def __init__(self, tamanho):
        self.fila = Queue(maxsize=tamanho)

    def inserir(self, item):
        self.fila.put(item)  # Bloqueia se a fila estiver cheia

    def retirar(self):
        return self.fila.get()  # Bloqueia se a fila estiver vazia
