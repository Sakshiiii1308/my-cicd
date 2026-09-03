import platform
import datetime

print("=== System Health Check ===")
print(f"Operating System: {platform.system()}")
print(f"Python Version: {platform.python_version()}")
print(f"Check Time: {datetime.datetime.now()}")

print("Application Status: HEALTHY")
print("CI/CD Practice Project: RUNNING")
