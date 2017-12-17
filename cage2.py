import prime_gen
import socket

from util import *

_g_SIZE = 4096

def connect(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Wait for connection acknowledge. Not sure this is necessary. Does s.connect() thread blcok?
        get_ACK(s)

        # compute b
        b = prime_gen.get_prime_private()

        # get p and g
        p = int.from_bytes(s.recv(_g_SIZE), byteorder='big', signed=False)
        send_ACK(s)

        g = int.from_bytes(s.recv(_g_SIZE), byteorder='big', signed=False)
        send_ACK(s)

        # get pA
        pa = int.from_bytes(s.recv(_g_SIZE), byteorder='big', signed=False)
        send_ACK(s)

        # send pB
        s.sendall(compute_power(p, b, g).to_bytes(_g_SIZE, byteorder='big'))
        get_ACK(s)

        return compute_power(pa, b, g)

