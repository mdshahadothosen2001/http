import socket
serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('localhost',8000))
serverSocket.listen(5)

while True:
    print('Server waiting for connections')
    (cSocket, address) = serverSocket.accept()
    print('HTTP server request received:')
    print(cSocket.recv(1024))
    cSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hello Md. Shahadot Hosen</h1><h6>This is from HTTP Server</h6></body></html>\r\n",'utf-8'))
    cSocket.close()