import dns.resolver

def check_domain(domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['1.1.1.1', '1.0.0.1']
    try:
        response = resolver.query(domain, 'NS')
        return len(response) != 0
    except:
        return False
