import socket
import sys
import time

server_add = ("0.0.0.0", 5555)
max_conexiones = 5
close_ser=''
sservidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sservidor.bind(server_add)
while close_ser!='y':
    #print ("Waiting connections ", server_add)

    print >> sys.stderr,'Waiting connections ',server_add

    sservidor.listen(max_conexiones)

    scli, cadd = sservidor.accept()

    nick=scli.recv(1024)

    #print("Connected to ", cadd)
    print>>sys.stderr,'\n--',nick,'has connected to the chat at',time.ctime(time.time()),'--\n'

    while True:

        rcvmsg = scli.recv(1024)
        if rcvmsg=="close":

            #print"Closing connection with ",cadd
            print >> sys.stderr,'\n...Closing connection with',nick,'at',time.ctime(time.time()),'...\n'
            close_ser=raw_input('Do you want to close Server(y/n)?')
            scli.close()
            break

        #print("Client says: ",msg)
        print >> sys.stderr,nick,':',rcvmsg


print>>sys.stderr,'\n--Server closed--\n'
#Close connection
sservidor.close()