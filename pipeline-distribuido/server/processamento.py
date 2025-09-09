# server/processamento.py

import threading
import time
from multiprocessing import Process
from server.fila import FilaLimitada
from utils.config import TAMANHO_FILA

# Filas para comunicação entre threads/processo
fila1 = FilaLimitada(TAMANHO_FILA)
fila2 = FilaLimitada(TAMANHO_FILA)

def thread_recebe(cliente_socket):
    while True:
        try:
            dados = cliente_socket.recv(1024).decode()
            if not dados:
                break
            print(f"[RECEBIDO] {dados}")
            fila1.inserir(dados)
        except:
            break

def processo_processa():
    while True:
        dado = fila1.retirar()
        print(f"[PROCESSANDO] {dado}")
        time.sleep(1)  # Simula tempo de processamento
        processado = f"[PROCESSADO] {dado.upper()}"
        fila2.inserir(processado)

def thread_responde(cliente_socket):
    while True:
        resposta = fila2.retirar()
        try:
            cliente_socket.send(resposta.encode())
        except:
            break
