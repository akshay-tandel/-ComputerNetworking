'''
TELE5360 Internet Protocol and Architecture

Assignment 1: Public Key Cryptography

Submitted by: Akshay Tandel (001280366)

The Object of this assigment is to create a client-server Python application that can be used to encrypt a file to be sent by a client and then to be decrypted on receiver side using public-key cryptography.

Server Program

'''

# Import Library
from socket import socket, AF_INET, SOCK_STREAM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Create a TCP socket 
socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('127.0.0.1', 11111))
socket.listen(1)

# Receive a encrypted data from client
csock, addr1 = socket.accept()
receive_data = csock.recv(1024)


with open("/home/akshay/assignment/key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend())

# Decrypt the ciphertext using private key
decrypted_text = private_key.decrypt(receive_data,
	padding.OAEP(
	mgf=padding.MGF1(algorithm=hashes.SHA1()),
	algorithm=hashes.SHA1(),
	label=None))

# Print the decrypted data
print "Decrypted Text:"
print decrypted_text

# Close the socket
socket.close()
	
