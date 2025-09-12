# 🧵 Sistema Distribuído de Gerenciamento de Produtos

Este projeto é uma aplicação simples de arquitetura **cliente-servidor** utilizando **Python**, **Sockets** e **Threads**, com foco nos conceitos de **concorrência**, **paralelismo** e **sincronização de acesso a recursos compartilhados**.

---

## 📌 Objetivo

Implementar um sistema distribuído onde múltiplos clientes podem se conectar a um servidor central para realizar operações em uma lista de produtos armazenada em memória. A comunicação é feita via `socket TCP` e cada cliente é tratado por uma thread dedicada. A sincronização de acesso à lista de produtos é feita com `threading.Lock`.

---

## ⚙️ Funcionalidades

- 📥 Adicionar produtos
- 📤 Remover produtos
- 📄 Listar produtos
- 👥 Suporte a múltiplos clientes simultâneos
- 🔒 Sincronização segura com `Lock`

---

## 📁 Estrutura do Projeto

```bash
.
├── server.py     # Código do servidor (roda e espera conexões)
└── client.py      # Código do cliente (envia comandos ao servidor)
```

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/LFPerylo/FCCPD-Projeto-1.git
cd produto-sistema
```

### 2. Execute o servidor

Em um terminal, rode:

```bash
python server.py
```

O servidor começará a escutar conexões na porta `5000`.

### 3. Execute os clientes

Em outros terminais (quantos quiser), rode:

```bash
python client.py
```

Você verá a mensagem de boas-vindas e poderá começar a interagir com o sistema.

---

## 💬 Comandos Disponíveis (no cliente)

| Comando                            | Descrição                                      |
|-----------------------------------|------------------------------------------------|
| `LISTAR`                          | Lista todos os produtos disponíveis            |
| `ADICIONAR nome preco quantidade` | Adiciona um novo produto                       |
| `REMOVER nome`                    | Remove um produto pelo nome                    |
| `SAIR`                            | Encerra a conexão com o servidor               |

> Exemplo:
> `ADICIONAR caneta 2.50 100`

---

## 🔐 Concorrência e Sincronização

- Cada cliente é tratado em uma **thread separada** usando `threading.Thread`.
- A lista de produtos é um recurso **compartilhado** e seu acesso é protegido com `threading.Lock` para evitar condições de corrida (race conditions).

---

## 🧪 Testes Recomendados

- Execute 2 ou mais clientes simultaneamente
- Tente adicionar e remover produtos ao mesmo tempo
- Verifique se a lista de produtos permanece consistente

---

## 🛠️ Requisitos

- Python 3.7 ou superior
- Sistema operacional: Windows, Linux ou MacOS

---

## 📄 Licença

Este projeto é de uso acadêmico para a disciplina de Fundamentos de Computação Concorrente, Paralela e Distribuída - CESAR School, 2025.2.

---

## 👨‍🏫 Professor responsável

**Jorge Soares**  
📧 jsfj@cesar.school
