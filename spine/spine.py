#!/usr/bin/env python

 #################################################
 # Scan OR, CRLF, CORS and others on Large Scan  #
 # by: Intercept9                                #
 # twitter.com/_SiddhuVarma                      #
 # http://intercept9.gitlab.io/                  #
 #################################################

import urllib2
import sys
import os
import threading
import Queue
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import init, Fore, Back, Style


class Spine:
	def __init__(self):
		self.Redirlist = ("https://example.com", "http://example.com", "http://www.example.com", "https://www.example.com")
		self.threads = []
		self.payloads = open('orpayloads.txt', 'r').read().splitlines()
		self.input_file = open(sys.argv[1],"r").read().splitlines()
		self.queue = Queue.Queue()
		self.lock = threading.Lock()
		self.kill = False
		self.thread_count = 20
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

	def banner(self):
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

	def reqUrl(self, req_data):
		try:
			r = requests.get("http://%s%s" % (req_data[0],req_data[1]),verify=False, allow_redirects=True,timeout=3)
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			resurl=r.url
			self.lock.acquire()
			try:
				if "https://example.com" in resurl:
					print (Style.RESET_ALL+Fore.GREEN+Style.DIM+"[+] "+req_data[0]+Fore.YELLOW+" Vulnerable "+"Payload ->"+Fore.CYAN+" http://"+req_data[0]+req_data[1]+Style.RESET_ALL).strip()
				else:
					print (Style.RESET_ALL+Fore.RED+Style.DIM+"[-] "+req_data[0]+Fore.RED+" Not Vulnerable "+"Payload ->"+Fore.CYAN+" http://"+req_data[0]+req_data[1]+Style.RESET_ALL).strip()
			finally:
				self.lock.release()
		except:
			pass

	def worker(self):
		while True:
			if self.queue.empty() != True:
				self.reqUrl(self.queue.get())
			else:
				print(Style.RESET_ALL+Fore.RED+Style.DIM+"[+] Stopping threads..." + Style.RESET_ALL)


	def main(self):
		self.banner()
		for target_domain in self.input_file:
			for payload in self.payloads:
				self.queue.put([target_domain, payload])
		for i in range(self.thread_count):
			t = threading.Thread(target=self.worker, args=())
			t.daemon = True
			self.threads.append(t)
			t.start()

		for thread in self.threads:
			thread.join()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python spine.py inputlist")
        sys.exit()
    else:
		keep_running = True
		print (Fore.YELLOW+"[-] Starting OpenRedirection Check..."+"\n")
		spine = Spine()
		try:
			spine.main()
		except KeyboardInterrupt:
			keep_running = False
	        try:
	            sys.exit(0)
	        except SystemExit:
	            os._exit(0)
