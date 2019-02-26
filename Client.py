# Name: Karteek Gole (1001553522)
# Reference: https://realpython.com/python-sockets/
#            https://docs.python.org/3/howto/sockets.html
#            http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
#            https://www.geeksforgeeks.org/socket-programming-python/

import socket
import time

TCP_IP_ADDRESS = input("Enter Host IP Address : ")             # For taking IP Address input from the user
TCP_PORT_NUMBER = int(input("Enter Port Number : "))                  # For taking Port no input from the user
BUFFER_SIZE = 1024

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Client socket object creation
tcpsocket.connect((TCP_IP_ADDRESS, TCP_PORT_NUMBER))              # Establishing a connection with the Server using the
                                                                  # Ip Address and port number
print("Connected to the Server")

file = input("Enter Filename : ")                              # Enter the file to be requested from the Server
print("\nHostname : ", socket.gethostname())
print("Port Number : ", TCP_PORT_NUMBER)
print("The Host IP Address : ", TCP_IP_ADDRESS)
print("The filename : ", file)
print("Peer name : "+str(tcpsocket.getpeername()))

tcpsocket.send(b'msg /'+file.encode())                         # Sending filename and requesting it from the server
Starttime = time.time()                                        # Time of the request
while True:                                                    # This While loop handles the incoming file
    content = tcpsocket.recv(BUFFER_SIZE)                      # Content check
    if not content:
        break                                                  # Break the loop if there is no content in the file
    print(content)
Endtime = time.time()                                              # Record time when the file was received for RTT calculation
rdtriptime = Endtime - Starttime                                   # Calculate the Round Trip Time (RTT)

print("\nRound Trip Time (RTT) : "+str(rdtriptime) + " Seconds ")   #Print calculated Round Trip Time
print('Socket Family : '+str(tcpsocket.family))                     #Print Socket Family
print('Socket Protocol : '+str(tcpsocket.proto))                    #Print the protocol name
print('Socket Type : '+str(tcpsocket.type))                         #Print Socket Type
print('Time out : '+str(tcpsocket.timeout))                         #Total time out
tcpsocket.close()                                                   # Close the Client Socket
print('\nThe Connection is closed')
