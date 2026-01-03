#example 1
# Converting string to integer

routerid = "3"                 # String
routeridnumber = int(routerid) # Convert to integer

print(type(routerid))          # str
print(type(routeridnumber))    # int

# Converting integer to string

vlan = 3
vlans = str(vlan)

print(type(vlan))              # int
print(type(vlans))             # str

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Example 2

# Sometimes input or data comes as a string
# We convert it to other data types when needed

vlan_id = "100"          # string
port_count = "48"        # string

# Convert string to integer
vlan_id_int = int(vlan_id)
port_count_int = int(port_count)

print(vlan_id_int, type(vlan_id_int))
print(port_count_int, type(port_count_int))
