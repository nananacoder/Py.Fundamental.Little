'''
Take the following IPv4 address: 128.32.10.1 This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.

  ip_to_int32("128.32.10.1") => 2149583361

Test.expect(ip_to_int32("128.114.17.104") == 2154959208, "wrong integer for ip: 128.114.17.104")
Test.expect(ip_to_int32("0.0.0.0") == 0, "wrong integer for ip: 0.0.0.0")
Test.expect(ip_to_int32("128.32.10.1") == 2149583361, "wrong integer for ip: 128.32.10.1")
'''

def ip_to_int32(ip):
    ip = [bin(int(i)) for i in ip.split('.')]
    res = ''
    for i in ip:
        if len(i)<10:
            i = (10-len(i))*'0'+i[2:]
            res += i
        else:
            res +=i[2:]
    print res
    return int(res,2)


def ip_to_int32_2(ip):
    import socket, struct
    """
       Convert an IP string to long
       """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

ip = "128.31.10.1"
print ip_to_int32(ip)