#!/usr/bin/python3
import subprocess
from urllib import request
import xml.etree.ElementTree as ET
import re
import os
import zipfile
import stat

'''
Google Chrome
'''
proc = subprocess.run(['google-chrome', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
res = proc.stdout.decode('utf-8').strip()
prog = re.compile("^Google Chrome ([0-9]+).*$")
match = re.fullmatch(prog, res)
if match is None:
    raise Exception('Google version not compliant: ' + res)
current_chrome_version = int(match.group(1))

'''
Chromedriver
'''
version_to_download = ''
url = "https://chromedriver.storage.googleapis.com/"
f = request.urlopen(url)
tree = ET.ElementTree(ET.fromstring(f.read()))
root = tree.getroot()
prog = re.compile("^([0-9]+)\\..*chromedriver_linux64.zip$")
for child in root:
    for sub in child:
        if sub.tag[-3:] == 'Key':
            match = re.fullmatch(prog, sub.text)
            if match is not None:
                version = int(match.group(1))
                if version == current_chrome_version:
                    version_to_download = sub.text

if version_to_download == '':
    raise Exception('Version not found: ' + str(current_chrome_version))

print('Version found: ' + version_to_download)

'''
Download and install
'''
tmp_zip_name = '/tmp/chromedriver_' + str(current_chrome_version) + '.zip'
if os.path.exists(tmp_zip_name):
    os.remove(tmp_zip_name)
request.urlretrieve(url + version_to_download, tmp_zip_name)
with zipfile.ZipFile(tmp_zip_name, "r") as zip_ref:
    zip_ref.extractall("/tmp")

chromedrive_tmp = '/tmp/chromedriver'
st = os.stat(chromedrive_tmp)
os.chmod(chromedrive_tmp, st.st_mode | stat.S_IEXEC)
os.system("sudo mv " + chromedrive_tmp + " /usr/local/bin/chromedriver")