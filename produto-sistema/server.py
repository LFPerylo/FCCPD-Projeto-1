# server.py
import socket
import threading
import datetime
from queue import Queue

produtos = []
lock = threading.Lock()
fila_comandos = Queue()

def log(msg):
    agora = datetime.datetime.now().strftime("%H:%M:%S")
    thread_id = threading.current_thread().name
    print(f"[{agora}][{thread_id}] {msg}")

# Estrutura do item na fila: (conn, comando_str)
def consumidor():
    while True:
        conn, dados = fila_comandos.get()
        if not dados:
            continue
        resposta = processar_comando(dados)
        try:
            conn.sendall(resposta.encode())
        except:
            log("Erro ao enviar resposta para cliente")

def tratar_cliente(conn, addr):
    log(f"Conexão com {addr}")
    conn.sendall("Bem-vindo ao sistema de produtos!\n".encode())

    while True:
        try:
            dados = conn.recv(1024).decode().strip()
            if not dados:
                break

            log(f"Recebido de {addr}: {dados}")
            fila_comandos.put((conn, dados))

            if dados.upper() == "SAIR":
                break
        except:
            break
    conn.close()
    log(f"Cliente {addr} desconectado")

def processar_comando(comando):
    partes = comando.split()
    if not partes:
        return "Comando inválido\n"

    operacao = partes[0].upper()

    if operacao == "LISTAR":
        with lock:
            log("Executando LISTAR")
            if not produtos:
                return "Nenhum produto cadastrado.\n"
            return "\n".join([
                f"{p['nome']} - R${p['preco']:.2f} - {p['quantidade']} unidades"
                for p in produtos
            ]) + "\n"

    elif operacao == "ADICIONAR" and len(partes) == 4:
        nome = partes[1]
        try:
            preco = float(partes[2])
            quantidade = int(partes[3])
        except ValueError:
            return "Preço ou quantidade inválidos.\n"
        with lock:
            log(f"Adicionando produto: {nome}, preço={preco}, qtd={quantidade}")
            produtos.append({
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade
            })
        return f"Produto {nome} adicionado com sucesso.\n"

    elif operacao == "REMOVER" and len(partes) == 2:
        nome = partes[1]
        with lock:
            for p in produtos:
                if p["nome"] == nome:
                    log(f"Removendo produto: {nome}")
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
    log(f"Servidor escutando em {host}:{porta}")

    consumidor_thread = threading.Thread(target=consumidor, name="Consumidor", daemon=True)
    consumidor_thread.start()

    while True:
        conn, addr = servidor.accept()
        cliente_thread = threading.Thread(target=tratar_cliente, args=(conn, addr), name=f"Cliente-{addr[1]}")
        cliente_thread.start()

if __name__ == "__main__":
    iniciar_servidor()
