#!/usr/bin/python3
# fronter.py 
# Written by Sanjiv Kawa / @kawabungah

from argparse import ArgumentParser
import requests
import sys

parser = ArgumentParser(description='Find Frontable Domains')
parser.add_argument('--domain', '-d', required=True, help='Your CDN endpoint')
parser.add_argument('--file', '-f', required=True, help='File containing domain names')

args = parser.parse_args()
filepath = args.file
hostHeader = args.domain

fileHandler = open (filepath, "r")
lines = fileHandler.readlines()
fileHandler.close()
        
print("[+] CDN Endpoint: " + hostHeader + "\n")
for domain in lines:
    domain = domain.strip()
    try:
        requests.get("https://" + domain + "/canary-" + domain, headers={'Host': hostHeader})
        print("[+] Testing: " + domain)
    except:
        print("[!] Testing: " + domain)
        continue


print('\n[+] Done!\nLogin to VPS and find your frontable domains\ncat /var/log/apache2/access.log | grep python-requests | awk -F"canary-" {\'print $2\'} | cut -d " " -f 1 | sort -u')
