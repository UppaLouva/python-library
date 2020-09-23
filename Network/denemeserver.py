import socket
sock=socket.socket()
sock.bind((socket.gethostname(),5000))
sock.listen(1)
client,addr=sock.accept()
print("Connection:",str(addr))
while 1:
    data=client.recv(1024).decode('utf-8')
    if not data:
        break
    print(data)

client.close()
