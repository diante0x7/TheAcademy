#!/usr/bin/python
import argparse
import os
import socket

# get the contents of the file we transfer
def get_file_contents(filename):
    try:
        with open(filename, 'rb') as fp:
            return fp.read()
    except:
            #print("File not found!")
            return False

parser = argparse.ArgumentParser(description="Peer-to-Peer File Transfer")
parser.add_argument('-f', '--filename', required=True, help="The file you intend to transfer")
parser.add_argument('-r', '--rhost', required=True, help="The ip address of the host you want to transfer to.")
parser.add_argument('-p', '--port', type=int, required=True, help="The port you want to connect to")
args = parser.parse_args()

filename = args.filename
host = args.rhost
port = args.port

file = get_file_contents(filename)
if file == False:
    print('File was not found! Please try again...')
    exit(1)
    
s = socket.socket()
try: s.connect((host, port))
except: print('Failed to connect to the server! Please try again.'); exit(1)
s.send(file)
s.close()
exit(0)