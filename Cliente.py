# -*- coding: utf-8 -*-
import socket
import sys

scliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serv_add = ("0.0.0.0", 5555)


#print("Connected to ", serv_add)
print >> sys.stderr, '\n--Connected to Server--\n'#,serv_add

scliente.connect(serv_add)

nick=raw_input("Choose NICK: ")
print>>sys.stderr,'\n'
scliente.send(nick)

while True:

    sndmsg = raw_input("me: ")
    scliente.send(sndmsg)

    if sndmsg == "close":
        break

print("\n--Disconnected--\n")
scliente.close()