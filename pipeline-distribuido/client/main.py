import socket
import threading
from utils.config import HOST, PORT

def escutar_respostas(sock):
    while True:
        try:
            resposta = sock.recv(1024).decode()
            if not resposta:
                break
            print(f"[SERVIDOR] {resposta}")
        except:
            print("Conexão encerrada.")
            break

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")

    # Inicia thread para escutar as respostas
    threading.Thread(target=escutar_respostas, args=(cliente,), daemon=True).start()

    # Loop de envio de mensagens
    while True:
        msg = input("Você: ")
        if msg.lower() == 'sair':
            break
        cliente.send(msg.encode())

    cliente.close()
    print("Conexão encerrada.")

if __name__ == "__main__":
    main()
