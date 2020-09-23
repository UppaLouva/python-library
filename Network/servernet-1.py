import socket as s

led_sock=s.socket(s.AF_INET,s.SOCK_STREAM)
led_sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)

host='192.168.0.13'
port=8080
led_sock.bind((host,port))
led_sock.listen(3)
client_ip,client_port = led_sock.accept()
while 1:
    data=client_ip.recv(1024).decode('utf-8')
    print(data)
    if not data:
        break
    data=data.upper()
    print("Sending: "+data)
    client_ip.send(data.encode('utf-8'))
client_ip.close()

