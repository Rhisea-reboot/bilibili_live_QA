import json
import urllib
import requests
import time

z = {}
xiaoxi = []
ren = []
posttext = set()
postren = set()

def get_live_room_info(room_id):
    url = f"https://api.live.bilibili.com/ajax/msg?roomid={room_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return {"error": f"请求失败，状态码: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    room_id = input("请输入直播间ID: ")
    while True:
        js = get_live_room_info(room_id)
        j = js["data"]["room"]
        jz = json.dumps(js["data"]["room"])
        for content in range(len(j)):
            nickname = j[content]["nickname"]
            text = j[content]["text"]
            #print (nickname,text,content)
            if j[content]["text"] not in posttext:
                xiaoxi.append(j[content])
                posttext.add(j[content]["text"])
                print(j[content]["text"])
        #print(result)
        time.sleep(10)
    print ("Finish!")
