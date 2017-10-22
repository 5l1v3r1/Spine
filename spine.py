#!/usr/bin/env python

 #################################################
 # Scan OR, CRLF, CORS and others on Large Scan  #
 # by: Intercept9                                #
 # twitter.com/_SiddhuVarma                      #
 # http://intercept9.gitlab.io/                  #
 #################################################

import requests
import sys
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import init, Fore, Back, Style
init()

def banner():
	
	print(Fore.GREEN+Style.DIM+"""

                    _,    _   _    ,_
               .o888P     Y8o8Y     Y888o.
              d88888      88888      88888b
             d888888b_  _d88888b_  _d888888b
             8888888888888888888888888888888
             8888888888888888888888888888888
             YJGS8P"Y888P"Y888P"Y888P"Y8888P
              Y888   '8'   Y8P   '8'   888Y
               '8o          V          o8'
                 `                     `
		  Coded by Intercept9
		""")

def operate(url,line,payload):
	try:
		r = requests.get(url,verify=False, allow_redirects=True,timeout=3)
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		resurl=r.url
		if "https://google.com/" in resurl:
			print ("========================================================================")
			print (Style.RESET_ALL+Fore.GREEN+Style.DIM+line+Fore.YELLOW+" Vulnerable "+"Payload -> "+Fore.CYAN+payload+Style.RESET_ALL).strip()
			print ("========================================================================")
		else:
			pass
	except:
		pass



def main(list):
	threads = []		
	with open('payloads.txt') as f:
		payloads = f.read().splitlines()
		file = open(list,"r")
		for line in file:
			for payload in payloads:
				domain = line.rstrip()
				furl = "http://"+domain+(payload.rstrip())
				print (Style.RESET_ALL+furl)
				operate(furl,domain, payload),payload



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python spine.py inputlist")
        sys.exit()
    else:
    	banner()
    	print (Fore.YELLOW+"[-] Starting OpenRedirection Check..."+"\n")
    	main(sys.argv[1])
