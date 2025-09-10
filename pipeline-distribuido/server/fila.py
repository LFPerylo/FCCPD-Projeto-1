# server/fila.py

import queue

class FilaLimitada:
    def __init__(self, tamanho_maximo):
        self.fila = queue.Queue(maxsize=tamanho_maximo)

    def inserir(self, item):
        print(f"\n[FILA] Inserindo item na fila")
        self.fila.put(item)

    def retirar(self):
        item = self.fila.get()
        print(f"\n[FILA] Retirado item da fila: {item}")
        return item
