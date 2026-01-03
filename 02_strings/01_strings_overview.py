#Example 2 
# Strings store text data
# Each character in a string has an index value
# Strings are IMMUTABLE (cannot be changed in place)

site = "chennai"   # Strings are always written inside quotes ""

print(site)
print(type(site))

# Using \n to move to a new line
ospf = "router ospf 1 \n is using router ID of 1.1.1.1 \n which is wrong"

print(ospf)

# Triple quotes can also be used for multi-line strings
ospf_config = """router ospf 1
is using router ID of 1.1.1.1
which is wrong"""

print(ospf_config)

#================================
#Example 2 

# Strings are used to store text data
# In network automation, strings are everywhere

router_name = "Chennai-Core-01"
router_ip = "10.10.10.1"
interface_name = "GigabitEthernet0/1"

print(router_name)
print(router_ip)
print(interface_name)

# Check data type
print(type(router_name))

