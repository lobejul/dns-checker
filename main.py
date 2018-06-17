import sys

from checker import Checker
from mailer import send_mail

def __main__():
    checker = Checker()
    target_mail = sys.argv[1]
    domain = sys.argv[2]
    success, result = checker.check_domain(domain)

    if success and not result:
        send_mail(target_mail, 'Domain available!', 'The domain {} is finally available!'.format(domain))

__main__()
