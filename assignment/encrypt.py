'''
TELE5360 Internet Protocol and Architecture

Assignment 1: Public Key Cryptography

Submitted by: Akshay Tandel (001280366)

The Object of this assigment is to create a client-server Python application that can be used to encrypt a file to be sent by a client and then to be decrypted on receiver side using public-key cryptography.

Client Program

'''


# Import library
from socket import socket, AF_INET, SOCK_STREAM
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Creat a TCP socket
s = socket(AF_INET, SOCK_STREAM)
server = ('127.0.0.1', 11111)
s.connect(server)

with open("/home/akshay/assignment/key.pem", "rb") as key_file:
	private_key = serialization.load_pem_private_key(
	key_file.read(),
	password=None,
	backend=default_backend())

# Generate the public key using private key
public_key = private_key.public_key()

# Open a file to read and encrypt data
read_file = open ('asn1.txt')
text = read_file.read()

# Print the plain text
print "Plan Text:"
print text

# Generate a ciphertext using public key
ciphertext = public_key.encrypt(text, padding.OAEP(
	mgf=padding.MGF1(algorithm=hashes.SHA1()),
	algorithm=hashes.SHA1(),
	label=None))

# Send a ciphertext to server
s.send(ciphertext)

#Print the encrypted text
print "Encrypted Text:"
print ciphertext

# Close the Client Socket
s.close()
