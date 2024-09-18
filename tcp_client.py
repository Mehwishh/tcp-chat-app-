import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.100.172',5000))  

print("Connected to the server!")


while True:
    message = input("You: ")  
    client_socket.send(message.encode('utf-8')) 

    server_message = client_socket.recv(1024).decode('utf-8')  
    if not server_message:  
        break
    print(f"Server: {server_message}")  

client_socket.close() 
