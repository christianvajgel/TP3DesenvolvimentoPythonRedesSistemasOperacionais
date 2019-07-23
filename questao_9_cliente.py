# TP3 - Desenvolvimento Python para Redes e Sistemas Operacionais [19E1_4] - Instituto Infnet.
# Christian Vajgel - 16/03/2019 - Thonny IDE
# questao_9_cliente

import socket, psutil, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()      
PORT = 9991
orig = (HOST, PORT)
quant = 1024

msg = "Dados armazenamento"

s.sendto(msg.encode('ascii'), orig)

data, addr = s.recvfrom(quant)
print("A quantidade de armazenamento total é de", data.decode('ascii'), "GB.")

data, addr = s.recvfrom(quant)
print("A quantidade de armazenamento disponível é de", data.decode('ascii'), "GB.")

s.close()