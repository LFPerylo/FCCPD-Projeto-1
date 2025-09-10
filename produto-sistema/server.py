# servidor.py
import socket
import threading

produtos = []
lock = threading.Lock()

def tratar_cliente(conn, addr):
    print(f"[+] Conectado com {addr}")
    conn.sendall("Bem-vindo ao sistema de produtos!\n".encode())
    while True:
        try:
            dados = conn.recv(1024).decode().strip()
            if not dados:
                break

            resposta = processar_comando(dados)
            conn.sendall(resposta.encode())
        except:
            break
    conn.close()
    print(f"[-] Cliente {addr} desconectado")

def processar_comando(comando):
    partes = comando.split()
    if not partes:
        return "Comando inválido\n"

    operacao = partes[0].upper()

    if operacao == "LISTAR":
        with lock:
            if not produtos:
                return "Nenhum produto cadastrado.\n"
            return "\n".join([f"{p['nome']} - R${p['preco']:.2f} - {p['quantidade']} unidades" for p in produtos]) + "\n"

    elif operacao == "ADICIONAR" and len(partes) == 4:
        nome = partes[1]
        try:
            preco = float(partes[2])
            quantidade = int(partes[3])
        except ValueError:
            return "Preço ou quantidade inválidos.\n"
        with lock:
            produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        return f"Produto {nome} adicionado com sucesso.\n"

    elif operacao == "REMOVER" and len(partes) == 2:
        nome = partes[1]
        with lock:
            for p in produtos:
                if p["nome"] == nome:
                    produtos.remove(p)
                    return f"Produto {nome} removido.\n"
        return f"Produto {nome} não encontrado.\n"

    elif operacao == "SAIR":
        return "Conexão encerrada.\n"

    return "Comando não reconhecido.\n"

def iniciar_servidor(host="127.0.0.1", porta=5000):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"Servidor escutando em {host}:{porta}")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
