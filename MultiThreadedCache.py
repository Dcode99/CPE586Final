# Import socket module
from socket import *
import requests

# import thread module
from _thread import *
import threading

# create a cache
cache = []


# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Defining serverSocket HOST and PORT, and listening
HOST = '127.0.0.1'
PORT = 32007
ThreadCount = 0
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

# Adding Multiple Client Functionality
def multi_threaded_client(connection):
    while True:
      # If an exception occurs during the execution of try clause
      # the rest of the clause is skipped
      # If the exception type matches the word after except
      # the except clause is executed
      try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024)

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        url = "http:/" + message.split()[1].decode()

        cached = False
        # Check if the url is cached, and if so return the data stored with code 200
        for entry in cache:
            if url == entry[0]:
                cached = True
                outputdata = entry[1]
                # test print to let user know it was cached
                print("returned from cache")

                # Send the HTTP response header line to the connection socket
                # Connection is successful if it gets here
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

                # Send the content of the requested file to the connection socket
                connectionSocket.sendall(outputdata)
                # for i in range(0, len(outputdata)):
                #    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())

                # Close the client connection socket
                # Thread count should drop on the close
                
                connectionSocket.close()
                break

        # if data isn't cached ask server for data
        if not cached:
            # This sends an http request to the initial server
            f = requests.get(url)
            # check if status is OK
            if f.status_code == 200:
                # Store the entire content of the requested file in a temporary buffer
                outputdata = f.content

                # add data to cache
                cache.append((url, outputdata))

                # Send the HTTP response header line to the connection socket
                # Connection is successful if it gets here
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

                # Send the content of the requested file to the connection socket
                connectionSocket.sendall(outputdata)
                connectionSocket.send("\r\n".encode())

                # Close the client connection socket
                # Thread count should drop on the close
                
                connectionSocket.close()
                break
            else:
                # send 404 not found if status is not okay
                connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())

                # Close the client connection socket

                # Thread count should drop on the close
                
                connectionSocket.close()
                break


      except IOError as err:
        print("IOError : {0}".format(err))

        # Send HTTP response message for file not found
       # connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())

        # Close the client connection socket
        # Thread count should drop on the close
        
        connectionSocket.close()
        break


# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve (Cache)...')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    
    # Thread section of main loop
    ThreadCount = ThreadCount + 1
    
    start_new_thread(multi_threaded_client, (connectionSocket, ))
    
    ThreadCount = ThreadCount - 1

    # new thread is started 
    
    print('Thread Number: ' + str(ThreadCount))

serverSocket.close()
