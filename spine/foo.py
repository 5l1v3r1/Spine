from fake_useragent import UserAgent
from fake_useragent import FakeUserAgentError


def random_useragent():
	try:
		ua = UserAgent()
		randomua = ua.random
		return randomua
	except FakeUserAgentError:
		pass


print random_useragent()



