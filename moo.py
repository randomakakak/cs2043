#! /usr/bin/env python

#server handle method processes incoming requests
#must instantiate server class, passing server address and request handler


import SocketServer
import socket
import sys
import threading

class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        socket.sendto("hi", self.client_address)

#class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass

def client(ip, port, message):
    data = message

    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.listen(5)
    # As you can see, there is no connect() call; UDP has no connections.
    # Instead, data is directly sent to the recipient via sendto().
    while True:
        sock.sendto(data + "\n", (HOST, int(sys.argv[3])))
        received = sock.recv(1024)
        print str(received)
        print "reach"
        if not received:
            print 'not received'
            break
        print "Sent:     {}".format(data)
        print "Received: {}".format(received)



if __name__ == "__main__":
    HOST, PORT = "localhost", int(sys.argv[2])
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    ip, port = server.server_address


    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
   
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = sock.connect_ex(("localhost",int(sys.argv[3])))
    print result

    client(ip, port, "Hello World 1")
    print "end"


    server.shutdown()


"""
# game
'''
 Bulls and cows. A game pre-dating, and similar to, Mastermind.
'''
 
import random
 
digits = '123456789'
size = 4
chosen = ''.join(random.sample(digits,size))
#print chosen # Debug
print '''I have chosen a number from %s unique digits from 1 to 9 arranged in a random order.
You need to input a %i digit, unique digit number as a guess at what I have chosen''' % (size, size)
guesses = 0
while True:
    guesses += 1
    while True:
        # get a good guess
        guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
        if len(guess) == size and \
           all(char in digits for char in guess) \
           and len(set(guess)) == size:
            break
        print "Problem, try again. You need to enter %i unique digits from 1 to 9" % size
    if guess == chosen:
        print '\nCongratulations you guessed correctly in',guesses,'attempts'
        break
    bulls = cows = 0
    for i in range(size):
        if guess[i] == chosen[i]:
            bulls += 1
        elif guess[i] in chosen:
            cows += 1
    print '  %i Bulls\n  %i Cows' % (bulls, cows)
"""
