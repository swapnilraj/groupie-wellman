_ACK = b'ack'

def send_ACK(conn):
    conn.sendall(_ACK)

def get_ACK(conn):
    return conn.recv(1024) == _ACK

def compute_power(base, power, mod):
    return pow(base, power, mod)
