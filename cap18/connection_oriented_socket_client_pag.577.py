import socket


IP_ADDR = 'localhost'
IP_PORT = 8881
MESSAGE = """\
A few lines of text
including non-ASCII charathers: $£
to test the operation
of both server
and client.
"""

encoding = 'utf-8'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((IP_ADDR, IP_PORT))
    print(f'Connected to server {IP_ADDR}:{IP_PORT}')
    for line in MESSAGE.splitlines():
        data = line.encode(encoding)
        sock.sendall(data)
        print(f'SENT {data!r} ({len(data)})')
        response, address = sock.recvfrom(1024)
        print(f'RCVD {response.decode(encoding)!r} ({len(response)}) from {address}')
print('Disconnected from server')
