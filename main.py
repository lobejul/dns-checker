import sys

from checker import check_domain
from mailer import send_mail
from settings import watched_domains, notify_mail

def __main__():
    for domain in watched_domains:
        occupied = check_domain(domain)

        if not occupied:
            send_mail(notify_mail, 'Domain available!', 'The domain {} is finally available!'.format(domain))

__main__()
