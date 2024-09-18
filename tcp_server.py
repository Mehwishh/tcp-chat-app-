import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.100.172',1024))  
server_socket.listen(5) 

print("Server started. Waiting for clients...")

client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    message = client_socket.recv(1024).decode('utf-8')  
    if not message: 
        break
    print(f"Client: {message}")  
    server_message = input("You: ") 
    client_socket.send(server_message.encode('utf-8')) 

client_socket.close()  
