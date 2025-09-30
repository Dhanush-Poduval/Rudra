import socket 
import threading

def handle_client(conn):
  def receive():
    while True:
      data=conn.recv(1024)
      if not data:
        print("Data not found")
        break
      print(f"Client: {data.decode()}",flush=True)
  def send():
    while True:
      msg=input("Server :")
      conn.sendall(msg.encode())
  threading.Thread(target=receive,daemon=True).start()
  threading.Thread(target=send,daemon=True).start()

host='127.0.0.1'
port =5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Server is listening")
conn,addr=s.accept()
print("Connected To ",addr)
handle_client(conn)
threading.Event().wait()
