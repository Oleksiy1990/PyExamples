import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 12345
BUFFER_SIZE = 1024
MESSAGE = 120

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(bytes(MESSAGE))
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)