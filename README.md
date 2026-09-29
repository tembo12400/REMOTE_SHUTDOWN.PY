# REMOTE_SHUTDOWN.PY
• Remote Shutdown: Automatically turns off a specific computer on the network using the target's IP address. • Remote Desktop Connection: Instantly opens the Windows Remote Desktop app (mstsc) and connects straight to the target computer.
# Windows Remote Management Tool

This Python script is a simple, lightweight tool for managing Windows computers on a local network. It uses standard Python libraries to help network administrators quickly turn off remote computers or start a Remote Desktop (RDP) connection.

## ✨ Features
* **Remote Shutdown:** Instantly turns off a specific network computer using its IP address.
* **Remote Desktop Connection:** Opens the Windows Remote Desktop app (`mstsc`) and auto-fills the target IP.
* **Safe Coding:** Includes built-in error handling to prevent crashes if a machine is offline.

## 📋 Requirements
For this script to work, ensure that:
1. Both computers are on the **same local network**.
2. You have **administrator access** on the target computer.
3. Remote Desktop and Remote Management are **enabled** in the target's Windows settings.

## 🚀 How to Use
1. Clone this repository to your computer.
2. Open the script and replace `192.168.1.10` with your target computer's IP address.
3. Uncomment the function you want to use (`shutdown_device` or `control_rdp`).
4. Run the script:
   ```bash
   python script.py
   ```
