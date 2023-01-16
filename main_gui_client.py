
import socket
from tkinter import *
from tkinter import ttk
import customtkinter

class Client:
    def __init__(self, master):
        self.master = master
        master.title("Client")

        self.label = customtkinter.CTkLabel(master, text="Enter a message to send to the server:")
        self.label.pack(side=TOP, fill=X, expand=YES, padx=20, pady=10)

        self.message_entry = customtkinter.CTkEntry(master)
        self.message_entry.pack()
        self.send_button = customtkinter.CTkButton(master, text="Send", command=self.send_message)
        self.send_button.pack()

        self.response_label = customtkinter.CTkLabel(master, text="Server response:")
        self.response_label.pack(side=BOTTOM, fill=X, expand=YES, padx=20)

        self.close_button = customtkinter.CTkButton(master, text="Close", command=self.close)
        self.close_button.pack(side=BOTTOM, fill=X, expand=YES, padx=20, pady=40)

        # create a socket to connect to the server
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "172.16.10.13"
        port = 9999
        self.clientsocket.connect((host, port))

    def send_message(self):
        # get the message from the entry widget
        message = self.message_entry.get()
        self.clientsocket.send(message.encode())

        # receive response from the server
        response = self.clientsocket.recv(1024).decode()

        # update the label with the server response
        self.response_label.configure(text="Server response: " + response)

    def close(self):
        self.clientsocket.close()
        self.master.destroy()


customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.geometry("300x400")
root.option_add('*font', ('verdana', 12, 'bold'))

client = Client(root)
root.mainloop()
