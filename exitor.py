#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "L4ser Secruity Labs"
__DATE__	= "31/01/2021"
__VERSION__	= "0.0.1"
__GITHUB__	= "https://github.com/L4ser-Security-Labs"

'''OSINT tool  for Nigerian Phone numbers'''

"""
    Copyright (C) 2020 L4ser Security Labs
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

from sys import path, argv
import argparse
import requests
from tqdm import tqdm
path.append("src")

parser = argparse.ArgumentParser(description = "Check if an IP address is a Tor exit node",\
				add_help = False)

parser.add_argument("-h", "--help", help = "Shows this message and exits",\
			action = "store_true")

parser.add_argument("-ip", help = "IP Address", 
                    type = str)

args = parser.parse_args()

DB_URL = "https://check.torproject.org/torbulkexitlist"
FNAME = ".exitor.txt"

def updatedb():
    print("Updating database...")
    resp = requests.get(DB_URL, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(FNAME, 'wb') as file, tqdm(
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)
    
def check_tor(ipaddress):
    print("Checking database...")
    with open(FNAME) as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            if ipaddress == line:
                return True
                

if __name__ == "__main__":
	import banner
	
	if len(argv) <= 1:
		parser.print_help()
		exit()
	else:
		if args.help == True:
			parser.print_help()
			exit()
		else:
			if args.ip == None:
				parser.print_help()
				print("\nexiTor: error: argument -ip is required\n")
				exit()
			else:
				pass
	print("\n")
	print("*" * 75)

if args.ip:
    updatedb()
    if check_tor(args.ip) == True:
        print(args.ip, "is a Tor exit node")
    else:
        print(args.ip, "is not a Tor exit node")
    exit()
