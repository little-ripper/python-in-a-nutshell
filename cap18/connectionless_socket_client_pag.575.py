import socket


UDP_IP = 'localhost'
UDP_PORT = 8883
MESSAGE = """\
This is a bunch of lines,
each of which will be sent in a single
UDP datagram. No error detection
or correction will occur.
Crazy bananas! £$
"""

server = UDP_IP, UDP_PORT
encoding = 'utf-8'
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    for line in MESSAGE.splitlines():
        data = line.encode(encoding)
        bytes_sent = sock.sendto(data, server)
        print(f'SENT {data!r} ({bytes_sent} of {len(data)}) to {server}')
    response, address = sock.recvfrom(1024)
    print(f'RCVD {response.decode(encoding)!r} from {address}')
print('Disconnected from server')
