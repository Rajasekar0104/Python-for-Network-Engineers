# Nested IF is used when multiple checks must pass in sequence

device_reachable = True
ssh_enabled = True
credentials_valid = False

if device_reachable:
    if ssh_enabled:
        if credentials_valid:
            print("✅ All checks passed – start automation")
        else:
            print("❌ Invalid credentials – stop execution")
    else:
        print("❌ SSH is disabled – cannot proceed")
else:
    print("❌ Device unreachable – abort automation")
