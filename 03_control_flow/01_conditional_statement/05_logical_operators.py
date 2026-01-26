# Logical operators combine multiple conditions

user_role = "admin"
device_type = "switch"
maintenance_window = True

if user_role == "admin" and maintenance_window:
    print("✅ Admin access granted during maintenance")

if device_type == "router" or device_type == "switch":
    print("📡 Network device supported")

if not maintenance_window:
    print("⛔ Changes blocked – outside maintenance window")
