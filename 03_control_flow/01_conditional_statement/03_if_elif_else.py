# IF-ELIF-ELSE handles multiple conditions

cpu_usage = 82  # Percentage

if cpu_usage < 50:
    print("✅ CPU usage is normal")
elif cpu_usage < 80:
    print("⚠️ CPU usage is high – monitor closely")
else:
    print("🚨 CPU usage is critical – take action immediately")
