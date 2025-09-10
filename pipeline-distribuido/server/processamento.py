# server/processamento.py

import time
import threading
from server.fila import FilaLimitada
from utils.config import TAMANHO_FILA

fila1 = FilaLimitada(TAMANHO_FILA)
fila2 = FilaLimitada(TAMANHO_FILA)

def thread_recebe(cliente_socket):
    print(f"[INICIADO] THREAD RECEBE   | ID: {threading.get_ident()} | Nome: {threading.current_thread().name}\n")
    while True:
        try:
            dados = cliente_socket.recv(1024).decode()
            if not dados:
                break
            print(f"\n[THREAD RECEBE] Recebido: {dados}\n")
            fila1.inserir(dados)
        except Exception as e:
            print(f"[ERRO RECEBE] {e}")
            break

def thread_processa():
    print(f"[INICIADO] THREAD PROCESSA | ID: {threading.get_ident()} | Nome: {threading.current_thread().name}\n")
    while True:
        try:
            dado = fila1.retirar()
            print(f"\n[THREAD PROCESSA] Processando: {dado}\n")
            time.sleep(1)
            processado = f"[PROCESSADO] {dado.upper()}"
            fila2.inserir(processado)
        except Exception as e:
            print(f"[ERRO PROCESSA] {e}")
            break

def thread_responde(cliente_socket):
    print(f"[INICIADO] THREAD RESPONDE | ID: {threading.get_ident()} | Nome: {threading.current_thread().name}\n")
    while True:
        try:
            resposta = fila2.retirar()
            print(f"\n[THREAD RESPONDE] Enviando: {resposta}\n")
            cliente_socket.send(resposta.encode())
        except Exception as e:
            print(f"[ERRO RESPONDE] {e}")
            break
