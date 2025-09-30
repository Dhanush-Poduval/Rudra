import socket
import threading

def receive(sock):
   while True:
     data=sock.recv(1024)
     if not data:
       print("Data not found")
       break
     print(f"Server : {data.decode()} ",flush=True)

def send(sock):
  while True:
    msg=input("Client : ")

    sock.sendall(msg.encode())
host='127.0.0.1'
port=5000
sock=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
sock.connect((host,port))

threading.Thread(target=receive,args=(sock,),daemon=True).start()

threading.Thread(target=send,args=(sock,),daemon=True).start()
threading.Event().wait()
