"""
Print all possible /28 subnets contained with 10.200.2.0/24 using python
"""

import ipaddress

v4nets=list(ipaddress.ip_network('10.200.2.0/24').subnets(new_prefix=28))
print("subnets: ")
for x in v4nets:
    print(x.with_prefixlen)
