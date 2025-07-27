#!/usr/bin/env python
# coding: utf-8

# # Advanced GUI-Based Chat Application

# #### Note: Install Necessary Libraries. Make sure you have Tkinter installed.

# In[1]:


get_ipython().system('pip install tk')


# ## Server Code

# In[2]:


import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

clients = []

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            display_message(message)
        except:
            break

def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)

def send_message():
    message = message_entry.get()
    message_entry.delete(0, tk.END)
    for client in clients:
        client.send(message.encode())

# GUI setup
root = tk.Tk()
root.title("Server Chat")

chat_window = scrolledtext.ScrolledText(root, state='disabled')
chat_window.pack(padx=20, pady=10)

message_entry = tk.Entry(root)
message_entry.pack(padx=20, pady=10)
message_entry.bind("<Return>", lambda event: send_message())

server_thread = threading.Thread(target=start_server)
server_thread.start()

root.mainloop()


# ## Client Code

# In[3]:


import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_client():
    client_socket.connect(('localhost', 12345))
    threading.Thread(target=receive_messages).start()

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            display_message(message)
        except:
            break

def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)

def send_message():
    message = message_entry.get()
    message_entry.delete(0, tk.END)
    client_socket.send(message.encode())

# GUI setup
root = tk.Tk()
root.title("Client Chat")

chat_window = scrolledtext.ScrolledText(root, state='disabled')
chat_window.pack(padx=20, pady=10)

message_entry = tk.Entry(root)
message_entry.pack(padx=20, pady=10)
message_entry.bind("<Return>", lambda event: send_message())

client_thread = threading.Thread(target=start_client)
client_thread.start()

root.mainloop()


# ### Install ipywidgets: We can use ipywidgets to help manage the Tkinter event loop.

# In[4]:


get_ipython().system('pip install ipywidgets')


# ## Update the server and client code to integrate with ipywidgets:-

# ## For the server:

# In[5]:


import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import ipywidgets as widgets
from IPython.display import display

clients = []

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            display_message(message)
        except:
            break

def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)

def send_message():
    message = message_entry.get()
    message_entry.delete(0, tk.END)
    for client in clients:
        client.send(message.encode())

def run_server_gui():
    root = tk.Tk()
    root.title("Server Chat")

    global chat_window
    chat_window = scrolledtext.ScrolledText(root, state='disabled')
    chat_window.pack(padx=20, pady=10)

    global message_entry
    message_entry = tk.Entry(root)
    message_entry.pack(padx=20, pady=10)
    message_entry.bind("<Return>", lambda event: send_message())

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    root.mainloop()

run_button = widgets.Button(description="Run Server")
run_button.on_click(lambda b: run_server_gui())
display(run_button)


# ## For the client:

# In[6]:


import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import ipywidgets as widgets
from IPython.display import display

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_client():
    client_socket.connect(('localhost', 12345))
    threading.Thread(target=receive_messages).start()

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            display_message(message)
        except:
            break

def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)

def send_message():
    message = message_entry.get()
    message_entry.delete(0, tk.END)
    client_socket.send(message.encode())

def run_client_gui():
    root = tk.Tk()
    root.title("Client Chat")

    global chat_window
    chat_window = scrolledtext.ScrolledText(root, state='disabled')
    chat_window.pack(padx=20, pady=10)

    global message_entry
    message_entry = tk.Entry(root)
    message_entry.pack(padx=20, pady=10)
    message_entry.bind("<Return>", lambda event: send_message())

    client_thread = threading.Thread(target=start_client)
    client_thread.start()

    root.mainloop()

run_button = widgets.Button(description="Run Client")
run_button.on_click(lambda b: run_client_gui())
display(run_button)


# # Running the Server and Client:-

# ## Run the server code cell:
# ### --> Click the "Run Server" button that appears to start the server GUI.

# ## Run the client code cell:
# ### --> Click the "Run Client" button that appears to start the client GUI.
