#!/usr/bin/env python
# coding: utf-8

# # Basic Text-Based Chat Application

# ## Server Code:

# In[1]:


import socket
import threading

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'bye':
            break
        print(f"Client: {message}")
        response = input("You: ")
        client_socket.send(response.encode())
        if response.lower() == 'bye':
            break

    client_socket.close()
    server_socket.close()

# Run the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.start()


# ## Client Code

# In[2]:


import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to the server")

    while True:
        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == 'bye':
            break
        response = client_socket.recv(1024).decode()
        if response.lower() == 'bye':
            break
        print(f"Server: {response}")

    client_socket.close()

# Start the client
start_client()

