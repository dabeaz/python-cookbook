from socket import AF_INET, AF_INET6, inet_pton, inet_ntop

def cidr_range(cidr_address):
    family = AF_INET6 if ':' in cidr_address else AF_INET
    address, maskstr = cidr_address.split('/')
    maskbits = int(maskstr)

    # Parse the supplied address into bytes
    addr_bytes = inet_pton(family, address)

    # Calculate number of address bytes and mask bits
    addr_len = len(addr_bytes)
    numaddrs = 2**(addr_len*8 - maskbits)
    mask = -numaddrs

    # Generate addresses
    addr = int.from_bytes(addr_bytes, 'big') & mask
    for n in range(numaddrs):
        yield inet_ntop(family, (addr+n).to_bytes(addr_len, 'big'))

if __name__ == '__main__':
   for a in cidr_range('123.45.67.89/27'):
       print(a)

   for a in cidr_range('12:3456:78:90ab:cd:ef01:23:34/125'):
       print(a)
