import socket
s=socket.socket()
print("Socket successfully created")
ip='127.0.0.1'
#creating the port to send stuff too

port=1234
s.bind((ip,port))

print("socket binded to %s"%(port))

s.listen(5)
conn,addr=s.accept()
print("socket is listening")
while True:
  data,addr=conn.recvfrom(1024)
  msg=data.decode()
  print(f"Got connection from {ip} :{msg}")
s.close()

