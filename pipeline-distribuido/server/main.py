# server/main.py

import socket
import threading
from server.processamento import thread_recebe, thread_processa, thread_responde
from utils.config import HOST, PORT

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f"[SERVIDOR] Ouvindo em {HOST}:{PORT}...")

    cliente_socket, endereco = servidor.accept()
    print(f"[SERVIDOR] Cliente conectado: {endereco}")

    # Inicia 3 threads: recebe, processa, responde
    threading.Thread(target=thread_recebe, args=(cliente_socket,), daemon=True).start()
    threading.Thread(target=thread_processa, daemon=True).start()
    threading.Thread(target=thread_responde, args=(cliente_socket,), daemon=True).start()

    while True:
        pass

if __name__ == "__main__":
    iniciar_servidor()
