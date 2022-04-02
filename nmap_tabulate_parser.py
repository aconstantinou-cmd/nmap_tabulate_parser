import argparse
import os
import sys
import xml.etree.ElementTree as ET
from tabulate import tabulate


def get_args():
    parser = argparse.ArgumentParser(description='Nmap XML parser')
    parser.add_argument('-f', '--file', help='Nmap XML file', required=True)
    parser.add_argument('-o', '--open', help='Print only open ports', required=False, action='store_true')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    if os.path.isfile(args.file):
        tree = ET.parse(args.file)
        root = tree.getroot()
        table = []
        for host in root.findall('host'):
            for address in host.findall('address'):
                if address.get('addrtype') == 'ipv4':
                    ip = address.get('addr')
            for port in host.findall('ports/port'):
                port_id = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                service = port.find('service').get('name')
                if args.open:
                    if state == 'open':
                        table.append([ip, port_id, protocol, state, service])
                else:
                    table.append([ip, port_id, protocol, state, service])
        print(tabulate(table, headers=['IP', 'Port', 'Protocol', 'State', 'Service']))
    else:
        print('File not found')
        sys.exit(1)


if __name__ == '__main__':
    main()

