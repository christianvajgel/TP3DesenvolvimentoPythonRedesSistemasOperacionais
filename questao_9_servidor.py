# TP3 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 16/03/2019 - Thonny IDE
# questao_9_servidor

import socket, psutil, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()      
PORT = 9991
orig = (HOST, PORT)
quant = 1024

armazenamento_total = str(round(psutil.disk_usage(os.getcwd()).total/1024**3))
armazenamento_disponivel = str(round(psutil.disk_usage(os.getcwd()).free/1024**3))

s.bind(orig)

print("Servidor aguardando conexão na porta", PORT, "...")

while True:
    (msg, cliente) = s.recvfrom(quant)
    print(msg.decode('ascii'))
    
    s.sendto(armazenamento_total.encode('ascii'), cliente)
    s.sendto(armazenamento_disponivel.encode('ascii'), cliente)

s.close()