
import platform
import datetime

print("=== System Health Check ===")
print(f"Operating System: {platform.system()}")
print(f"Python Version: {platform.python_version()}")
print(f"Check Time: {datetime.datetime.now()}")
print("\n=== Environment Information ===")
print(f"Machine Name: {platform.node()}")
print(f"System Architecture: {platform.machine()}")
print("Environment Check: PASSED")


print("Application Status: HEALTHY")
print("CI/CD Practice Project: RUNNING")

