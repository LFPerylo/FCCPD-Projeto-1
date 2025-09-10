# server/fila.py

import queue
import threading

class FilaLimitada:
    def __init__(self, limite):
        self.fila = queue.Queue(maxsize=limite)
        self.lock = threading.Lock()

    def inserir(self, item):
        with self.lock:
            self.fila.put(item)
            print("[FILA] Inserindo item na fila")

    def retirar(self):
        with self.lock:
            item = self.fila.get()
            print("[FILA] Retirando item da fila")
            return item
