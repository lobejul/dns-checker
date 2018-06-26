import sys

from checker import Checker
from mailer import send_mail
from settings import watched_domains, notify_mail

def __main__():
    checker = Checker()
    for domain in watched_domains:
        success, result = checker.check_domain(domain)

        if success and not result:
            send_mail(notify_mail, 'Domain available!', 'The domain {} is finally available!'.format(domain))

__main__()
