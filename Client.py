# Name: Karteek Gole (1001553522)
# Reference: https://realpython.com/python-sockets/
#            https://docs.python.org/3/howto/sockets.html
#            http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
#            https://www.geeksforgeeks.org/socket-programming-python/

import socket
import time

TCP_IP_ADDRESS = input("Enter Host IP Address : ")             # For taking IP Address input from the user
TCP_PORT = int(input("Enter Port Number : "))                  # For taking Port no input from the user
BUFFER_SIZE = 1024

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Client socket object creation
tcpsocket.connect((TCP_IP_ADDRESS, TCP_PORT))                     # Establishing a connection with the Server using the
                                                                  # Ip Address and port number
print("Connected to the Server")

file = input("Enter Filename : ")                              # Enter the file to be requested from the Server
print("\nHostname : ", socket.gethostname())
print("Port Number : ", TCP_PORT)
print("The Host IP Address : ", TCP_IP_ADDRESS)
print("The filename : ", file)
print("Peer name : "+str(tcpsocket.getpeername()))

tcpsocket.send(b'msg /'+file.encode())                         # Requesting file from the Server
Start = time.time()                                            # Store the time at which the request was made
while True:                                                    # While loop handles the incoming file from the Server
    content = tcpsocket.recv(BUFFER_SIZE)                         # Read the contents of the file
    if not content:                                            # If no content is present in the file
        break                                                  # Break the loop
    print(content)
End = time.time()                                              # Store the time at which the file was received
rtt = End - Start                                              # Calculate the Round Trip Time (RTT)

print("\nRound Trip Time (RTT) : "+str(rtt) + " Seconds ")
print('Socket Family : '+str(tcpsocket.family))
print('Socket Protocol : '+str(tcpsocket.proto))
print('Socket Type : '+str(tcpsocket.type))
print('Time out : '+str(tcpsocket.timeout))
tcpsocket.close()                                                  # Close the Client Socket
print('\nThe Connection is closed')
