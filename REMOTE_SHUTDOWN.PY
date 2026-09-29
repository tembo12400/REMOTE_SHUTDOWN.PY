import os
import subprocess

def shutdown_device(target_ip):
    subprocess.call(["shutdown", "/s", "/t", "0", "/m", f"\\\\{target_ip}"])

def control_rdp(target_ip):
    os.system(f"mstsc /v:{target_ip}")

# TEMBO12400
shutdown_device("192.168.1.10")  # Replace with target IP
control_rdp("192.168.1.10")  
"""
TEMBO 12400 
OR TRY
import os, subprocess

# Define functions in a single line
shut = lambda ip: subprocess.call(["shutdown", "/s", "/t", "0", "/m", f"\\\\{ip}"])
rdp  = lambda ip: os.system(f"mstsc /v:{ip}")

# Set IP and run both commands
ip = "192.168.1.10"
shut(ip)
rdp(ip)
"""

