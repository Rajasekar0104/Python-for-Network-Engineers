#Example 1
# input() is used to take user input
# Input is ALWAYS treated as a string

vlan = input("enter the value : ")

print("the most used vlan is VLAN", vlan)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Example 2

# input() is used to take user input
# Input is ALWAYS received as a string

router_name = input("Enter router name: ")
router_ip = input("Enter router IP: ")

print("Router Name:", router_name)
print("Router IP:", router_ip)

# Confirm data type
print(type(router_name))
print(type(router_ip))
