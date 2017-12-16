from sympy import randprime

def get_min_max_bit_size(bit):
    return (int(('1' + '0' * (bit - 1)), 2), int(('1' * bit), 2))

def get_prime_p():
    range_start, range_end = get_min_max_bit_size(1024)
    return randprime(range_start, range_end)

def get_prime_g():
    range_start, range_end = get_min_max_bit_size(4096)
    return randprime(range_start, range_end)

def get_prime_private():
    range_start, range_end = get_min_max_bit_size(256)
    return randprime(range_start, range_end)
