import dns.resolver
from concurrent.futures import ThreadPoolExecutor


target_domain = 'example.com'

subdomains = ['www', 'mail', 'ftp', 'blog', 'test', 'dev']

def check_subdomain(subdomain):
    try:
        full_domain = f"{subdomain}.{target_domain}"
        results = dns.resolver.resolve(full_domain, 'A')  
        addresses = [ip.address for ip in results]
        if addresses:
            print(f"Subdomain found: {full_domain} with IP: {', '.join(addresses)}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No record found for {full_domain}")
    except Exception as e:
        print(f"Error resolving {full_domain}: {e}")


with ThreadPoolExecutor(max_workers=10) as executor:
    for subdomain in subdomains:
        executor.submit(check_subdomain, subdomain)
