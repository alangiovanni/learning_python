import socket
# Portas DEFAULT da nossa máquina
print(socket.getservbyname("domain"))
print(socket.getservbyname("http"))
print(socket.getservbyname("ftp"))
print(socket.getservbyname("ssh"))