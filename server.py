import socket
host = '192.168.43.5'
port = 5000
addr = (host,port)
#print(addr)
server_socket = socket.socket()
server_socket.bind(addr)
server_socket-listen()
