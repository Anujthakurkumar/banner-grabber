#! /usr/bin/python3

import socket
tcp_address=input ("what ip address do u want to collect banner from ? ")



port=int(input("what port  u want to collect banner from ? "))


first_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

first_socket.connect((tcp_address, port))

banner = first_socket.recv(1024)
print(banner)

first_socket.close()