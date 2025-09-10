# client/main.py

import socket
import threading
from datetime import datetime
from utils.config import HOST, PORT

def escutar_respostas(sock):
    while True:
        try:
            resposta = sock.recv(1024).decode()
            if resposta:
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"\r{' '*60}\r[{timestamp}] [SERVIDOR] {resposta}\nVocê: ", end="")
        except Exception as e:
            print(f"[ERRO ESCUTA] {e}")
            break

def main():
    nome = input("Digite seu nome: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        print("[CLIENTE] Iniciando conexão com o servidor...")
        sock.connect((HOST, PORT))
        print(f"[CLIENTE] Conectado ao servidor em {HOST}:{PORT}")

        # Envia o nome do cliente ao servidor
        sock.send(f"__nome__:{nome}".encode())

        threading.Thread(target=escutar_respostas, args=(sock,), daemon=True).start()
        print("[CLIENTE] Thread de escuta iniciada")

        while True:
            msg = input("Você: ")
            if msg.strip():
                sock.send(msg.encode())

if __name__ == "__main__":
    main()
