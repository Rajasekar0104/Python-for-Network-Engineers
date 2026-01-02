# Mutable data types can be modified without changing memory location
# Lists are mutable

interfaces = ["Gi0/0", "Gi0/1"]

# Initial state
print("Interfaces before update:", interfaces)
print("Memory ID before:", id(interfaces))

# Modifying the list (adding a new interface)
interfaces.append("Gi0/2")

# Updated state
print("Interfaces after update:", interfaces)
print("Memory ID after:", id(interfaces))
