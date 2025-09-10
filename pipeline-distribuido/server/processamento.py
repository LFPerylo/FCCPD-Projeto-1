# server/processamento.py

import time
import threading
from server.fila import FilaLimitada

# Funções para cada cliente

def thread_recebe(cliente_socket, fila_entrada, nome_cliente):
    print(f"[THREAD RECEBE - {nome_cliente}] ID: {threading.get_ident()} | Nome: {threading.current_thread().name}")
    while True:
        try:
            dados = cliente_socket.recv(1024).decode()
            if not dados:
                break
            print(f"[THREAD RECEBE - {nome_cliente}] Recebido: {dados}")
            fila_entrada.inserir(dados)
        except Exception as e:
            print(f"[ERRO RECEBE - {nome_cliente}] {e}")
            break

def thread_processa(fila_entrada, fila_saida, nome_cliente):
    print(f"[THREAD PROCESSA - {nome_cliente}] ID: {threading.get_ident()} | Nome: {threading.current_thread().name}")
    while True:
        try:
            dado = fila_entrada.retirar()
            print(f"[THREAD PROCESSA - {nome_cliente}] Processando: {dado}")
            time.sleep(1)
            processado = f"[PROCESSADO] {dado.upper()}"
            fila_saida.inserir(processado)
        except Exception as e:
            print(f"[ERRO PROCESSA - {nome_cliente}] {e}")
            break

def thread_responde(cliente_socket, fila_saida, nome_cliente):
    print(f"[THREAD RESPONDE - {nome_cliente}] ID: {threading.get_ident()} | Nome: {threading.current_thread().name}")
    while True:
        try:
            resposta = fila_saida.retirar()
            print(f"[THREAD RESPONDE - {nome_cliente}] Enviando: {resposta}")
            cliente_socket.send(resposta.encode())
        except Exception as e:
            print(f"[ERRO RESPONDE - {nome_cliente}] {e}")
            break
