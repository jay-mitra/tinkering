# The Simple Client
# This is the client half of my final project, and it uses meets the following criteria:
# (1) Include a function that takes at least two user arguments from the command line
# (2) Have one try/except clause for every function
# (3) Output something (write) to a file, using string formatting (this one is a sort of, a scoket is kind of like a file, right?)

# I just realised I basically implemented a telnet client in python :| lol

import sys
import socket

def send(conn):
    """Uses the input socket to send user input to the server"""
    try:
        conn.send(input("Send to the server :").encode())
    except Exception as e:
        print ("The following error occurred: {}".format(e))

if __name__ == "__main__":
    """Initiates the Simple Client, sending user input string one line at a time to the Simple Server. To run you should start the Simple Server first, and then connect to the same hostname and port using the Simple Client. For example: simple_client.py localhost 50010 if you started the Simple Server using simple_server.py 50010"""
    try:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                send(s)
    except socket.error as e:
        print ("Failed to connect, with an error of \"{}\", is the server running?".format(e))
    except IndexError:
        print ("Not enough arguments provided, you need to run simple_client.py followed by the hostname and port to send to. For example: simple_client.py localhost 50010")
    except Exception as e:
        print ("Yeah, something super weird happened, apparently the error was: \"{}\".".format(e))
