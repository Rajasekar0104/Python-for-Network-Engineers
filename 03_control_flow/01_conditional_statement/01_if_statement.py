# IF is used when an action is required only if a condition is true

interface_status = "up"

# Check if interface is operational
if interface_status == "up":
    print("✅ Interface is UP – traffic can flow")
