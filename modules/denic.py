from module import Module
from requests import post

class Denic(Module):
    def __init__(self):
        super(Denic, self).__init__(['de'])

    def check_domain(self, domain):
        payload = {'lang': 'de', 'domain': domain}
        result = post('https://www.denic.de/webwhois/', payload).text
        return (True, (' ist bereits registriert.' in result))
