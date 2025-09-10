# server/main.py

import socket
import threading
from server.processamento import thread_recebe, thread_processa, thread_responde
from server.fila import FilaLimitada
from utils.config import HOST, PORT, TAMANHO_FILA

def lidar_com_cliente(cliente_socket, endereco):
    try:
        # Recebe a primeira mensagem e extrai o nome do cliente
        identificacao = cliente_socket.recv(1024).decode().strip()
        if identificacao.startswith("__nome__:"):
            nome_cliente = identificacao.replace("__nome__:", "")
        else:
            nome_cliente = "Desconhecido"

        print(f"\n[SERVIDOR] Cliente '{nome_cliente}' conectado de {endereco}\n")

        # Cria filas individuais para o cliente
        fila_entrada = FilaLimitada(TAMANHO_FILA)
        fila_saida = FilaLimitada(TAMANHO_FILA)

        # Inicia threads para esse cliente
        threading.Thread(target=thread_recebe, args=(cliente_socket, fila_entrada, nome_cliente), daemon=True).start()
        threading.Thread(target=thread_processa, args=(fila_entrada, fila_saida, nome_cliente), daemon=True).start()
        threading.Thread(target=thread_responde, args=(cliente_socket, fila_saida, nome_cliente), daemon=True).start()

    except Exception as e:
        print(f"[ERRO CLIENTE] {e}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[SERVIDOR] Ouvindo em {HOST}:{PORT}...")

    while True:
        cliente_socket, endereco = servidor.accept()
        threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco), daemon=True).start()

if __name__ == "__main__":
    iniciar_servidor()