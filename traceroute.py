# implement traceroute from scratch, as per https://en.wikipedia.org/wiki/Traceroute#Implementations

import sys
import socket
# import random
# import time

# use args from console to start the trace
def main(destination):
    try:
        print (socket.gethostbyname(destination))
    except Exception as e:
        print ("Can't find {}".format(e))

# generate a tracer object
class Tracer():
    def __init__(self, dst):
        pass

# the tracer should establish a socket to the destination

# we will probably need a listener as well

# STRETCH: depending on whether the user wants to use ICMP or TCP, fork the methods

# it should loop, incrementing the ttl by 1 to map out the route
    def hop(self):
        pass

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print ("Please supply a destination to trace")
