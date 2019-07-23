# TP3 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 16/03/2019 - Thonny IDE
# questao_10_11_cliente

import socket, os

HOST = socket.gethostname()
PORT = 8881
HP = (HOST, PORT)
qnt = 4096

def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = "Baixando arquivo... "
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_arq = input('Entre com o nome do arquivo: ')

try:
    cliente.connect(HP)
    cliente.send(nome_arq.encode('ascii'))
    msg = cliente.recv(12)
    tamanho = int(msg.decode('ascii'))

    if tamanho >= 0:
        arq = open('C:\\Users\\user-admin\\Desktop' + nome_arq, "wb")
        soma = 0
        bytes = cliente.recv(qnt)
    
        while bytes:
            arq.write(bytes)
            soma = soma + len(bytes)
            os.system('cls')
            imprime_status(soma, tamanho)
            bytes = cliente.recv(qnt)
            arq.close()
    
    else:
        print("Este arquivo não existe no servidor!")

except Exception as erro:
    print(str(erro))
        
cliente.close()
input("Pressione qualquer tecla para sair...")