import socket 
ip='127.0.0.1'
port=1234
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
   s.connect((ip,port))
   while True:
     message=input("Enter message")
     s.sendall(message.encode('utf-8'))
   
   print(s.recv(1024).decode())
   s.close()
