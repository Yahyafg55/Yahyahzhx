import requests

chat_id = "1990588404"
urlp = "https://t.me/yahyahyy"
url = f"https://api.telegram.org/bot6969577050:AAFeNsbUqhXzHMiHpB45f4DTTLWZWWDYhk8/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
