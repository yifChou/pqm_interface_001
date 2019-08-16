#coding=utf-8

import requests
url = "http://10.168.92.105:7721/api/Forecast/PacketOrder"
yt = "YT18257125121000039"
data={
    "shipper_hawbcode": yt,
    "actionCode": "Submit",
    "channelCode": "CollisimoFX"
}
headers = {'Content-Type': 'application/json' }
r = requests.post(url,data,headers)
print(r.text)