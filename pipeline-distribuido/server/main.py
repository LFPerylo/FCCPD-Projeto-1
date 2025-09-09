# server/main.py

import socket
import threading
from multiprocessing import Process
from server.processamento import thread_recebe, processo_processa, thread_responde
from utils.config import HOST, PORT

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f"[SERVIDOR] Ouvindo em {HOST}:{PORT}...")

    cliente_socket, endereco = servidor.accept()
    print(f"[SERVIDOR] Cliente conectado: {endereco}")

    # Thread A: recebe dados do cliente
    threading.Thread(target=thread_recebe, args=(cliente_socket,), daemon=True).start()

    # Processo B: processa dados
    Process(target=processo_processa, daemon=True).start()

    # Thread C: envia resposta para o cliente
    threading.Thread(target=thread_responde, args=(cliente_socket,), daemon=True).start()

    # Mantém o servidor vivo
    while True:
        pass

if __name__ == "__main__":
    iniciar_servidor()
