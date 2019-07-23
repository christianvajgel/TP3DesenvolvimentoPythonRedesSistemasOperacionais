# TP3 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 16/03/2019 - Thonny IDE
# questao_10_11_servidor

import socket, os

HOST = socket.gethostname()
PORT = 8881
HP = (HOST, PORT)
qnt = 4096

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(HP)

servidor.listen()
print("Servidor de nome", HOST, "esperando conexão na porta", PORT)

while True:
    (cliente,addr) = servidor.accept()
    print("Conectado ao cliente na porta", PORT, str(addr))

    msg = cliente.recv(2048) ###
    nome_arq = msg.decode('ascii')
    if os.path.isfile(nome_arq):

        tamanho = os.stat(nome_arq).st_size
        cliente.send(str(tamanho).encode('ascii'))

        arq = open(nome_arq, 'rb')

        bytes = arq.read(qnt)
        while bytes:
            cliente.send(bytes)
            bytes = arq.read(qnt)

        arq.close()
    else:
        print("Arquivo não encontrado.")

        cliente.send('-1'.encode('ascii'))

cliente.close()
servidor.close()