import socket
host = "192.168.43.4"
port = 5000
addr = (host,port)
server_socket = socket.socket()
server_socket.bind(addr)
server_socket.listen(5)
  

while True: 
   c, addr = server_socket.accept()
   data = c.recv(1024).decode()
   print ('client-> ', str(data)) 
   data = input('me-> ') 
   c.send(data.encode())
c.close() 
