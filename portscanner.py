#! usr/bin/python3.10

import socket, sys

# get the target IP or hostname from command line argument
target = sys.argv[1]

# generate a range of port numbers to scan
# NOTE: we are using a built-in function range() to generate numbers in the specified range
# but we are converting the range object to a list using the list() function and then using that
# list to iterate over the port numbers
port_numbers = list(range(1, 2001))

# define ANSI color codes for highlighting text in output
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

# iterate over each port number and try to connect to it
for port in port_numbers:
    try:
        # create a socket object for connecting to the port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # try to connect to the port
        if sock.connect_ex((target, port)) == 0:
            # if connection is successful, print the port number in green color
            print("[+] The Port {0} is {1}Opened{2}".format(YELLOW + str(port) + RESET, GREEN, RESET))
       # else:
            # if connection fails, print the port number in red color
           # print("[!] The port {0} is {1}Closed{2}".format(YELLOW + str(port) + RESET, RED, RESET))
    except socket.error:
        # if there's an error with the socket, print a message in red color
        print("[!] Error with Socket !")
