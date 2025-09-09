# server/processamento.py

import time
from server.fila import FilaLimitada
from utils.config import TAMANHO_FILA

# Filas compartilhadas entre threads
fila1 = FilaLimitada(TAMANHO_FILA)
fila2 = FilaLimitada(TAMANHO_FILA)

def thread_recebe(cliente_socket):
    print("[INICIADO] THREAD RECEBE")
    while True:
        try:
            dados = cliente_socket.recv(1024).decode()
            if not dados:
                break
            print(f"[THREAD RECEBE] Recebido: {dados}")
            fila1.inserir(dados)
        except Exception as e:
            print(f"[ERRO RECEBE] {e}")
            break

def thread_processa():
    print("[INICIADO] THREAD PROCESSA")
    while True:
        try:
            dado = fila1.retirar()
            print(f"[THREAD PROCESSA] Processando: {dado}")
            time.sleep(1)
            processado = f"[PROCESSADO] {dado.upper()}"
            fila2.inserir(processado)
        except Exception as e:
            print(f"[ERRO PROCESSA] {e}")
            break

def thread_responde(cliente_socket):
    print("[INICIADO] THREAD RESPONDE")
    while True:
        try:
            resposta = fila2.retirar()
            print(f"[THREAD RESPONDE] Enviando: {resposta}")
            cliente_socket.send(resposta.encode())
        except Exception as e:
            print(f"[ERRO RESPONDE] {e}")
            break
