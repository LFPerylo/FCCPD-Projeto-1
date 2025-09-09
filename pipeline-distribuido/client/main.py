# client/main.py

import socket
import threading
from utils.config import HOST, PORT

def escutar_respostas(sock):
    print("[CLIENTE] Thread de escuta iniciada")
    while True:
        try:
            resposta = sock.recv(1024).decode()
            if not resposta:
                break
            print(f"[SERVIDOR] {resposta}")
        except:
            print("[CLIENTE] Conexão encerrada pelo servidor.")
            break

def main():
    print("[CLIENTE] Iniciando conexão com o servidor...")
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    print(f"[CLIENTE] Conectado ao servidor em {HOST}:{PORT}")

    threading.Thread(target=escutar_respostas, args=(cliente,), daemon=True).start()

    while True:
        msg = input("Você: ")
        if msg.lower() == 'sair':
            break
        cliente.send(msg.encode())

    cliente.close()
    print("[CLIENTE] Conexão encerrada.")

if __name__ == "__main__":
    main()
