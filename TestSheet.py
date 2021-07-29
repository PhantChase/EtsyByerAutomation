import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib, json
import requests

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("etsyseller-sheet.json", scope)

client = gspread.authorize(creds)

sheet = client.open("VPS Etsy").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records


col = sheet.col_values(2)  # Get a specific column

def Convert(string):
    li = list(string.split(":"))
    return li
proxylistac = ['181.215.217.195:45785','134.202.250.38:45785']
i=0
e=1
for x in col:
    proxies = {"http": "http://Selphantridungdz:N7a8PfA@"+proxylistac[i]}
    try:
        if ":" in x:
            listproxy = Convert(x)
            xfinal = listproxy.pop(0)

        else:
            xfinal = x

        # with urllib.request.urlopen("http://ip-api.com/json/"+str(xfinal)) as url:
        #     data = json.loads(url.read().decode())
        #     print(data)
        r = requests.get("http://ip-api.com/json/"+str(xfinal), proxies=proxies)

        y = json.loads(r.content)
        print(y['country'])
        ipa = sheet.update('D'+str(e),y['country'])
        e+=1
    except:
        i+=1
        e += 1
