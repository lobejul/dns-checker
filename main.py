from checker import Checker

def __main__():
    checker = Checker()
    domain = input("Domain name to check: ")
    success, result = checker.check_domain(domain)
    
    if not success:
        print('No result for "{}" was found.'.format(domain))
    else:
        print('The domain is already registered' if result else 'The domain is available')

__main__()
