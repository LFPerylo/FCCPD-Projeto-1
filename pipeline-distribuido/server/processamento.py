import threading
import time
from multiprocessing import Process
from server.fila import FilaLimitada
from utils.config import TAMANHO_FILA

# Fila de entrada (thread A → processo B)
fila1 = FilaLimitada(TAMANHO_FILA)

# Fila de saída (processo B → thread C)
fila2 = FilaLimitada(TAMANHO_FILA)

def thread_recebe(cliente_socket):
    while True:
        dados = cliente_socket.recv(1024).decode()
        if not dados:
            break
        print(f"[RECEBIDO] {dados}")
        fila1.inserir(dados)

def processo_processa():
    while True:
        dado = fila1.retirar()
        print(f"[PROCESSANDO] {dado}")
        processado = f"[PROCESSADO] {dado.upper()}"
        time.sleep(1)  # Simula custo
        fila2.inserir(processado)

def thread_responde(cliente_socket):
    while True:
        resposta = fila2.retirar()
        cliente_socket.send(resposta.encode())
