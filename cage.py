import prime_gen
import socket

from util import *

_g_SIZE = 4096

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

def listen(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            send_ACK(conn)
            
            # Generate p and g
            p = prime_gen.get_prime_p()
            g = prime_gen.get_prime_g()
            a = prime_gen.get_prime_private()

            # send p and g
            conn.sendall(p)
            get_ACK(conn)
            
            conn.sendall(g)
            get_ACK(conn)

            # Send pA
            conn.sendall(compute_power(p, a, g).to_bytes(_g_SIZE, byteorder='big'))
            get_ACK(conn)

            # Get pB
            pb = int.from_bytes(conn.recv(_g_SIZE), byteorder='big', signed=False)
            send_ACK(conn)

            return compute_power(pb, a, g)
            
def __main__():
    ## if no args start the default
    if len(sys.argv) < 3:
        listen(HOST, PORT)
    else:
        listen(sys.argv[1], sys.argv[2])
