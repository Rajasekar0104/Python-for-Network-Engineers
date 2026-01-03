# Example 1

# String formatting is used to combine values cleanly
# f-strings are the recommended approach

vlan = input("enter the value : ")
switch = input("enter the hostname of the switch : ")

detail = f"the hostname of the switch is {switch} and it uses vlan number {vlan}"

print(detail)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# String formatting is cleaner and safer than concatenation
# Recommended approach for automation scripts

router_name = "Chennai-Core-01"
router_ip = "10.10.10.1"
ssh_port = 22

# f-string (Python 3.6+)
message = f"Connecting to {router_name} ({router_ip}) on port {ssh_port}"

print(message)
