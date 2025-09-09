# server/fila.py

from queue import Queue

class FilaLimitada:
    def __init__(self, tamanho):
        self.fila = Queue(maxsize=tamanho)

    def inserir(self, item):
        print("[FILA] Inserindo item na fila")
        self.fila.put(item)  # bloqueia se cheio

    def retirar(self):
        print("[FILA] Retirando item da fila")
        return self.fila.get()  # bloqueia se vazio
