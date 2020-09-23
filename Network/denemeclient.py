import socket 
sock=socket.socket()
sock.connect((socket.gethostname(),5000))
message=input("-->")
while message!='q':
    sock.send(message.encode('utf-8'))
    message=input("-->")
    
sock.close()


