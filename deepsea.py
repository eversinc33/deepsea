#!/usr/bin/python3
import sys 
from bs4 import BeautifulSoup

import requests
import argparse
from email.utils import getaddresses
import json

from requests import ConnectionError

types = ["email", "username", "name", "ip", "password", "uid"]

def find_leaks(search, search_type, phpsessid):
    url = "http://xjypo5vzgmo7jca6b322dnqbsdnp3amd24ybx26x5nxbusccjkm4pwid.onion/deepsearch"

    request_data = {'search': search, 'dropdownn': search_type, 'tsearchv': 'match'}

    r = session.post(url, data=request_data, cookies={'PHPSESSID':phpsessid})

    return parse_response(r)

def parse_response(response):
    html = response.text
    soup = BeautifulSoup(html, "lxml")

    td = soup.find_all('td')

    i = 0
    while i < len(td):
        first_item  = td[i].getText()
        second_item = td[i+1].getText()  
        
        # :^)
        if '/20' in first_item:
            print("")
        
        print(f"[*] {first_item}:\t {second_item}")
        i += 2

if __name__ == '__main__':

    print("""
@@@@@@@  @@@@@@@@ @@@@@@@@ @@@@@@@   @@@@@@ @@@@@@@@  @@@@@@ 
 @@!  @@@ @@!      @@!      @@!  @@@ !@@     @@!      @@!  @@@
 @!@  !@! @!!!:!   @!!!:!   @!@@!@!   !@@!!  @!!!:!   @!@!@!@!
 !!:  !!! !!:      !!:      !!:          !:! !!:      !!:  !!!
 :: :  :  : :: ::: : :: :::  :       ::.: :  : :: :::  :   : :
""")

    parser = argparse.ArgumentParser(prog=f'{sys.argv[0]}')
    parser.add_argument("--sid", help=f"value of your PHPSESSID cookie", type=str)
    parser.add_argument("--type", help=f"type to look for, default is email. possible values: {types}", type=str, default="email")
    parser.add_argument("--target", help="target to search for", type=str)
    parser.add_argument("--list", help="file with targets separated by newlines")
    parser.add_argument("--proxy", default='127.0.0.1:9050', type=str, help="Set Tor proxy (default: 127.0.0.1:9050)")
    args = parser.parse_args()

    # onion stuff
    proxy = args.proxy
    session = requests.session()
    session.proxies = {'http': f'socks5h://{proxy}', 'https': f'socks5h://{proxy}'}

    if not args.sid:
        print(f"[-] Add session id cookie via --sid flag")

    if args.type not in types:
       print(f"[-] Type must be one of {types}")
    
    if (not args.target and not args.list) or not args.type or not args.sid:
        parser.print_help()
        sys.exit(1)

    targets = []

    if args.target:
        targets.append(args.target)

    if args.list:
        lines = open(args.list).readlines()
        for line in lines:
            targets.append(line.split('\n')[0])

    for target in targets:
        print(f"\n[{target}] Searching for leaks...")
        find_leaks(target, args.type, args.sid)
