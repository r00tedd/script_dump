#!/usr/bin/env python

"""
icmp_subnet_sweep sends 1 icmp request to every IP address on a subnet, or a subset of the subnet if arguments are used.
argument 1 = IP address including subnet, but not the last octate (e.g 192.168.1)
argument 2 (optional) = Lower bound of IP range to scan (e.g 1)
argument 3 (optional) = Upper bound of IP range to scan (e.g 255)
"""

import argparse
import os
import sys

def ping(address):
    # os.system returns 0 of the address responds, so 'not' is required 
    return not os.system('ping %s -n 1' % (address,))

if __name__ == '__main__':

    ip_address = sys.argv[1]

    # If user does not include lower and upper bound for IP range, default to 0 - 255
    if (len(sys.argv) == 4):
        if int(sys.argv[2]) not in range(0, 256):
            raise ValueError("Your lower bound was invalid. Enter an int between 0 and 255.")
        ip_start = int(sys.argv[2])

        if int(sys.argv[3]) not in range(0, 256):
            raise ValueError("Your upper bound was invalid. Enter an int between 0 and 255.")
        ip_end = int(sys.argv[3])
    else:
        ip_start = 0
        ip_end = 255

    active_devices = []

    for i in range (ip_start, ip_end + 1):
        ip = (ip_address + '.' + str(i))
        if ping(ip):
            active_devices.append(ip)

    print('')
    print('Responding devices: ')
    print('')
    for i in active_devices:
        print(i)
    print('')
