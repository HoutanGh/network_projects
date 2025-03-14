import socket
from queue import Queue
import threading


# find open ports in servers, computers (any kind of host)
# open ports might be a security gap

target = '' # default gateway
queue = Queue()
open_ports = []

def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, using tcp
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    count = 0
    while not queue.empty():
        port = queue.get() # get next port in the list as it's not empty
        if port_scan(port):
            print(f'Port {port} is open!')
            open_ports.append(port)
            count += 1

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = [] 
for t in range(500):
    thread = threading.Thread(target=worker) #referring to worker function without calling it
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f'Open ports are: {open_ports}') # not printed until all threads are done




# for port in range(1, 1024):
#     result = port_scan(port)
#     if result:
#         print(f'Port {port} is open!')
#         count += 1
#     else:
#         print(f'Port {port} is closed!')


# print(port_scan(80)) # http
# print(port_scan(22)) # ssh
# print(port_scan(443)) # https
# print(port_scan(21)) # ftp
# print(port_scan(25)) # smtp
# print(port_scan(110)) # pop3
# print(port_scan(143)) # imap
# print(port_scan(3306)) # mysql
