import socket
host= "192.168.43.4"
port=5000

client_socket=socket.socket()
client_socket.connect((host,port))

data = input("-> ")
while True: 
   client_socket.send(data.encode())
   data = client_socket.recv(1024).decode()
   print ('sender-> ', str(data)) 
   data = input('me-> ') 
   
client_socket.close()



