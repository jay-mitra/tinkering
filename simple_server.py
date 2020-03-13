# The Simple Server
# This is the server half of my final project, and it uses meets the following criteria:
# (1) Have one try/except clause for every function
# (2) Read in and Process a file (this one is a sort of, a socket is kind of like a file, right?)

import sys
import socket

def receive(conn):
    """Uses the input socket to listen to input from the client"""
    data = conn.recv(1024)
    if not data:
        raise socket.error
    print ("Received from the client :{}".format(data.decode()))

if __name__ == "__main__":
    """Initiates the Simple Server, which listens on the specified port for a raw connection, and will echo to the terminal whatever it receives decoding it to an (assumed) utf8 encoding. Designed to work with the Simple Client which sends it lines of utf8 encoded strings, however will work with something like telnet as well"""
    try:
        HOST = "localhost" # Only really makes sense for the server to listen on its own host
        PORT = int(sys.argv[1])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            while True:
                receive(conn)
    except ValueError:
        print ("Looks like you didn't provide an integer for the listening port. Try something like 50010")
    except IndexError:
        print ("Not enough arguments provided, you need to run simple_server.py followed by the port to listen on. For example: simple_server.py 50010")
    except socket.error:
        print ("The client disconnected.")
    except Exception as e:
        print ("Yeah, something super weird happened, apparently the error was: \"{}\".".format(e))
