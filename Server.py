# Name: Karteek Gole (1001553522)
# Reference: https://realpython.com/python-sockets/
#            https://docs.python.org/3/howto/sockets.html
#            http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
#            https://www.geeksforgeeks.org/socket-programming-python/

import socket
import threading
import sys

MSG_BUFFER_SIZE = 1024                                              # Defining standard Buffer size for incoming messages
TCP_IP_ADDRESS = "localhost"                                    # Defining IP address of the Server (localhost at 127.0.0.1)
TCP_PORT_NUMBER = int(input("Enter Port Number: "))                    # Port no for accepting cnxns


class Thread(threading.Thread):                                 # Thread class, here we set up cnxns with the 1 or n-clients
    def __init__(self, ip, port, sock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("Client IP address : " + ip + " Port Number:" + str(
            port))                                              # Print IP address and Port Number for the respective clients

    def run(self):                                              # method run defines the processing of client request
        try:
            request = self.sock.recv(MSG_BUFFER_SIZE)               # This is the request from the connected client
            print(request)
            filename = request.split()[1]                       # Retrieving file name that the client fed
            print("File that was requested is:", filename[1:])
            file = open(filename[1:])                           # Open file
            data = file.read()                                  # Reading contents of the file and storing it to be displayed
            file.close()                                        # Closing the file
            print("Content of the file:", data)
            self.sock.send(b'HTTP/1.1 200 OK')                  # Status code #200 is the file is found
            self.sock.send(data.encode())                       # Encode and send the data back over to be displayed
            print('The File has been sent successfully')
            self.sock.close()                                   # Close Client socket
        except IOError:
            self.sock.send(b'HTTP/1.1 404 Not Found')           # Status code #404 if the file is not found
            print("File not found (don't forget adding .html to filename)")
            self.sock.close()                                   # Closing the Client socket


tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Server socket object named tcpsocket
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
threads = [];                                                   # To handle multiple Client connections

try:
    tcpsocket.bind((TCP_IP_ADDRESS, TCP_PORT_NUMBER))                    # Bind Server socket to the IP address and the port number
    print('Server bind is Complete')

except socket.error as msg:
    print(msg)  # Display error message if server binding failed
    sys.exit()

tcpsocket.listen(100)                                               # Initializing the Server socket to listen to incoming Client connections
print('Server is ready to accept connections')

while True:
    cnxn, address = tcpsocket.accept()                      # Establish the connection
    print("\nClient is connected with Ip Address:"
          + address[0] + ' and port number:' + str(address[1]))
    print(cnxn)
    print("Host name: " + str(cnxn.getpeername()))
    print('Socket Family: ' + str(cnxn.family))             #Print Socket Family
    print('Socket Type: ' + str(cnxn.type))                 #Print the socket type
    print('Time out: ' + str(cnxn.timeout))                 #Print total timeout
    print('Socket Protocol: ' + str(cnxn.proto))            #Print the protocol name (using lib native function proto)
    conn = Thread(address[0], address[1], cnxn)
    conn.start()
    threads.append(conn)                                        # Appending the new connection
