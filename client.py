import socket
import select
import errno
from threading import Thread

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

# Create a socket
# IPv4, TCP connection (connection-based)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state
client_socket.setblocking(False)

# Find out username size in bytes to set a fixed size and send it
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

def listen_for_messages():
	while True:

		try:
			username_header = client_socket.recv(HEADER_LENGTH)

			if not len(username_header):
				print('Connection closed by the server')
				sys.exit()

			# Convert header to int value
			username_length = int(username_header.decode('utf-8').strip())

			# Receive and decode username
			username = client_socket.recv(username_length).decode('utf-8')

			#Checking length of message isn't required
			message_header = client_socket.recv(HEADER_LENGTH)
			message_length = int(message_header.decode('utf-8').strip())
			message = client_socket.recv(message_length).decode('utf-8')

			
			print(f'{username} > {message}')
			
		    
			#message = client_socket.recv(1024).decode()
			#print("\n" + message)
		except IOError as e:
			# error.EAGAIN - no incoming data, try again
		# error.EWOULDBLOCK - either send buffer is full while sending or receive buffer is empty while receiving
			if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
				print('Reading error: {}'.format(str(e)))
				sys.exit()
                         # if nothing is received
			continue


# prints messages received by client
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
# daemon thread - background service thread which runs in low priority
t.daemon = True
t.start()

while True:
	message = input()
	# Repeat same username operation but for message
	message = message.encode('utf-8')
	message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
	client_socket.send(message_header + message)

