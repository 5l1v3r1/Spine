import multiprocessing

def operate(s,a,b):
	print s+a+b

def max():
	furl="master"
	domain="slave"
	payload="heha"
	proc = multiprocessing.Process(target=operate,args=(furl,domain, payload))
	proc.start()
	proc.join()

def main():
	max()

if __name__ == '__main__':
	main()