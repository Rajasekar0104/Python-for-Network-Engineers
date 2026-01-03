#Example 1

# Concatenation means joining values using +

vlan = 4
vlan_id = "server"

print(vlan)

# This will FAIL because int + str is not allowed
# print(vlan + vlan_id)

# Fix by converting integer to string
print(str(vlan) + vlan_id)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Example 2
# Concatenation means joining strings

site = "Chennai"
device_type = "Router"

# Using + operator
device_name = site + "-" + device_type + "-01"

print(device_name)

# Adding space manually
message = "Connecting to " + device_name
print(message)
