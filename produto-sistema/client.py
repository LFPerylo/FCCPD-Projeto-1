# client.py
import socket

def cliente_loop(host="127.0.0.1", porta=5000):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((host, porta))
    except ConnectionRefusedError:
        print("Erro: não foi possível se conectar ao servidor.")
        return

    print(cliente.recv(1024).decode())

    while True:
        comando = input("Digite um comando (LISTAR, ADICIONAR, REMOVER, SAIR): ").strip()
        if not comando:
            continue

        try:
            cliente.sendall(comando.encode())

            resposta = cliente.recv(4096)
            if not resposta:
                print("Servidor encerrou a conexão.")
                cliente.close()
                break

            resposta = resposta.decode()
            print(resposta)

            if "Conexão encerrada" in resposta:
                cliente.close()
                break

        except BrokenPipeError:
            print("Erro: o servidor encerrou a conexão.")
            break
        except ConnectionResetError:
            print("Conexão foi encerrada pelo servidor.")
            break

if __name__ == "__main__":
    cliente_loop()
