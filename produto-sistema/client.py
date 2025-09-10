# cliente.py
import socket

def cliente_loop(host="127.0.0.1", porta=5000):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    print(cliente.recv(1024).decode())

    while True:
        comando = input("Digite um comando (LISTAR, ADICIONAR, REMOVER, SAIR): ")
        cliente.sendall(comando.encode())
        resposta = cliente.recv(4096).decode()
        print(resposta)
        if "Conexão encerrada" in resposta:
            break

    cliente.close()

if __name__ == "__main__":
    cliente_loop()
