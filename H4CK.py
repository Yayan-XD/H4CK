#!/usr/bin/python2
# coding=utf-8
#Code by Yayan-XD
#created 07-02-20

try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 h4ck.py')

### LEMPANG ###
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)

### IYE KONTOL ###
logo ='''\n\x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\n
 \x1b[1;92m█████████       \x1b[1;97m  ╭\x1b[1;94m━━━━━━━━━━━━━━━\x1b[1;97m╮
 \x1b[1;92m█▄█████▄█        \x1b[1;97m │\x1b[1;97mLOGIN PASS+USER\x1b[1;97m│      
 \x1b[1;92m█ \x1b[1;93m▼▼▼▼▼\x1b[1;97m- _ --_--  ╰\x1b[1;94m━━━━━━━━━━━━━━━\x1b[1;97m╯
 \x1b[1;94m█\x1b[1;97m  _-_-- -_ --__    ╭\x1b[1;91m━━━━━━━━━━━\x1b[1;97m╮
 \x1b[1;94m█\x1b[1;93m ▲▲▲▲▲\x1b[1;97m--  - _ --   │\x1b[1;92mLOGIN TOOLS\x1b[1;97m│ 
 \x1b[1;94m█████████         \x1b[1;97m  ╰\x1b[1;91m━━━━━━━━━━━\x1b[1;97m╯   
 \x1b[1;97m██    ██    \x1b[1;91m•\x1b[1;93m•\x1b[1;92m•\x1b[1;97m DEVELOPMENT BY YAYAN XD \x1b[1;92m•\x1b[1;93m•\x1b[1;91m•
\x1b[1;94m────────────────────────────────────────────────────'''

os.system('clear')
CorrectUsername = 'YayanXD'
CorrectPassword = 'YayanXD'

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input('\n\033[1;32m Username Login\033[1;31m : \x1b[00m')
    if (username == CorrectUsername):
    	password = raw_input('\033[1;32m Password Login \033[1;31m: \x1b[00m')
        if (password == CorrectPassword):
            jalan('   \n\033[1;37m Orang paling ganteng Adalah\033[1;32m YayanXD') 
            time.sleep(1)
            loop = 'false'
        else:
            print '\n  \033[1;31m Wrong Password'
            time.sleep(2)
            os.system('xdg-open https://www.facebook.com/KM39453')
            os.system('clear')
    else:
        print '\n  \033[1;31m Wrong Username'
        time.sleep(2)
        os.system('xdg-open https://www.facebook.com/KM39453 ')
        os.system('clear')

def kontol():
    jalan('\n \033[1;33mPLEASE WAIT 2MINUTES, ALL PACKAGES ARE CHECKING...')
    os.system('python2 KONTOL/login.py')
       
       
if __name__ == '__main__':
   kontol()
