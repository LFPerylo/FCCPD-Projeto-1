
# Sistema Distribuído: Chat Simples com Arquitetura Cliente-Servidor

Este é um projeto prático que demonstra a implementação de um sistema distribuído usando uma arquitetura **cliente-servidor** e aplicando conceitos de **concorrência** com **threads**. O objetivo é criar um chat simples onde o cliente envia mensagens para o servidor, que as processa e as envia de volta.

## ⚙️ Arquitetura e Conceitos

A solução é dividida em três componentes principais:

1.  **Cliente**: Responsável pela interface com o usuário. Ele permite que o usuário digite mensagens e as envia para o servidor. Para garantir que ele possa receber respostas a qualquer momento, ele utiliza **duas threads**: uma para enviar mensagens e outra para escutar as respostas do servidor.

2.  **Servidor**: O "cérebro" do sistema. Ele aceita conexões e gerencia o fluxo de mensagens. Sua principal característica é o uso de **três threads dedicadas** para processar as mensagens de forma concorrente:

      * **Thread `recebe`**: Fica em um loop infinito, esperando e recebendo mensagens do cliente.
      * **Thread `processa`**: Retira as mensagens recebidas, realiza um "processamento" (neste caso, converte a mensagem para maiúsculas) e as prepara para serem enviadas de volta.
      * **Thread `responde`**: Envia a mensagem processada de volta ao cliente.

3.  **Filas (`Queue`)**: As threads do servidor se comunicam de forma segura e síncrona usando **filas compartilhadas**. Isso é um mecanismo de **sincronização** que evita que as threads colidam ou tentem acessar dados de forma errada. As filas garantem que as mensagens são recebidas, processadas e respondidas em uma ordem correta.

Essa arquitetura de múltiplas threads permite que o servidor continue recebendo novas mensagens mesmo enquanto processa e responde às mensagens antigas, tornando o sistema mais robusto e eficiente.

-----

## 🚀 Como Executar o Projeto

Para testar o sistema, siga os passos abaixo. Certifique-se de que você tem o Python 3 instalado em sua máquina.

### 1\. Iniciar o Servidor

Abra um terminal, navegue até a pasta `server` e execute o arquivo `main.py`:

```bash
cd server
python main.py
```

Você verá a mensagem: `[SERVIDOR] Ouvindo em 127.0.0.1:5555...`

**Atenção:** Mantenha este terminal aberto. O servidor precisa estar em execução para que o cliente possa se conectar.

### 2\. Iniciar o Cliente

Abra um **segundo terminal**, navegue até a pasta `client` e execute o arquivo `main.py`:

```bash
cd client
python main.py
```

Você verá a mensagem: `[CLIENTE] Conectado ao servidor em 127.0.0.1:5555`.

Agora você pode começar a digitar suas mensagens.

### 3\. Testando o Chat

  * Digite uma mensagem no terminal do cliente e pressione `Enter`.
  * Você verá a mensagem ser enviada para o servidor, processada e devolvida com o texto em maiúsculas.
  * Para sair, basta digitar `sair` no terminal do cliente e pressionar `Enter`.
