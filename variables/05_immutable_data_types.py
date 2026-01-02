# Immutable data types cannot be changed in-place
# Strings are immutable

router_name = "Core-Router"

# Memory ID before change
print("Original Router Name:", router_name)
print("Original ID:", id(router_name))

# Updating the value creates a new object in memory
router_name = router_name + "-01"

# Memory ID after change
print("Updated Router Name:", router_name)
print("New ID:", id(router_name))
