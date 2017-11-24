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

Redirlist = ("https://google.com", "http://google.com", "http://www.google.com", "https://www.google.com")
Redirbuff = []
Crlfbuff = []

def Redirector(url,line,payload):
	try:
		r = requests.get(url,verify=True, allow_redirects=True,timeout=3)
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		resurl=r.url
		for re in Redirlist:
			if resurl.startswith(re):
				print ("===================================================================")
				print ("[+] "+Style.RESET_ALL+Fore.GREEN+Style.DIM+line+Fore.YELLOW+" Vulnerable "+"Payload -> "+Fore.CYAN+payload+Style.RESET_ALL).strip()
				print ("===================================================================")
				Redirbuff.append(line)
		else:
			pass
	except:
		pass
	

def InitiateRedir(list):
	with open('orpayloads.txt') as f:
		payloads = f.read().splitlines()
		file = open(list,"r")
		for line in file:
			for payload in payloads:
				domain = line.rstrip()
				furl = "http://"+domain+(payload.rstrip())
				print (Style.RESET_ALL+furl)
				Redirector(furl,domain, payload)


def GenerateRedirBuf():
	testbuf = []
	for red in Redirbuff:
		if red not in testbuf:
			testbuf.append(red)
	return testbuf

'''
CRLF Routine

def InitiateCRLF(list):
	with open ('crlfpayloads') as f:
		payloads = f.read().splitlines()
		file = open(list,"r")
'''

def main(list):
	# Flag parse and do redir and crlf checks
	InitiateRedir(list)		
	

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python spine.py inputlist")
        sys.exit()
    else:
    	print ("\n"+Fore.YELLOW+"[-] Initiating OpenRedirection Check..."+"\n")
    	try:
    		main(sys.argv[1])
    		print ("\n\n")
    		print GenerateRedirBuf()		
    	except KeyboardInterrupt:
    		print(Style.RESET_ALL+Fore.GREEN+Style.DIM+"\r\n[+] Finished!"+Style.RESET_ALL)
    		try:
    			sys.exit(0)
	        except SystemExit:
	            os._exit(0)
