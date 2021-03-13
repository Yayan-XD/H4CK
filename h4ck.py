#!/usr/bin/python2
# coding=utf-8
#Code by Yayan-XD
#created 07-02-2021

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
logo ='''\n\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m•\x1b[1;97m\n
 \x1b[1;94m█████████       \x1b[1;97m  ╭\x1b[1;91m━━━━━━━━━━━━━\x1b[1;97m╮
 \x1b[1;94m█▄█████▄█        \x1b[1;97m │\x1b[1;94m TOOLS LOGIN \x1b[1;97m│      
 \x1b[1;94m█ \x1b[1;93m▼▼▼▼▼\x1b[1;97m- _ --_--  ╰\x1b[1;91m━━━━━━━━━━━━━\x1b[1;97m╯
 \x1b[1;94m█\x1b[1;97m  _-_-- -_ --__   ╭\x1b[1;91m━━━━━━━━━━\x1b[1;97m╮ 
 \x1b[1;94m█\x1b[1;93m ▲▲▲▲▲\x1b[1;97m--  - _ --  │\x1b[1;92mUSER+PASS\x1b[1;97m │ 
 \x1b[1;91m█████████         \x1b[1;97m ╰\x1b[1;91m━━━━━━━━━━\x1b[1;97m╯   
 \x1b[1;97m██ ██
\x1b[1;94m────────────────────────────────────────────────────'''

os.system('clear')
CorrectUsername = 'Yayan-XD'
CorrectPassword = 'Yayan-XD'

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input('\n \033[1;37m[\033[1;32m•\033[1;37m] Username Login : \033[1;33m')
    if (username == CorrectUsername):
    	password = raw_input(' \033[1;37m[\033[1;32m•\033[1;37m] Password Login : \033[1;33m')
        if (password == CorrectPassword):
            jalan('\n\033[1;37m [\033[1;36m*\033[1;37m] Orang paling ganteng Adalah\033[1;32m YayanXD') 
            time.sleep(1)
            loop = 'false'
        else:
            print '\n\033[1;37m [\033[1;31m!\033[1;37m] Wrong Password'
            time.sleep(2)
            os.system('xdg-open https://github.com/Yayan-XD/H4CK')
            os.system('clear')
    else:
        print '\n\033[1;37m [\033[1;31m!\033[1;37m] Wrong Username'
        time.sleep(2)
        os.system('xdg-open https://github.com/Yayan-XD/H4CK')
        os.system('clear')

def kontol():
    jalan('\n\033[1;37m [\033[1;36m*\033[1;37m] PLEASE WAIT 2 MINUTES INSTALLING COMMANDS...')
    os.system('python2 KONTOL/login.py')
       
       
if __name__ == '__main__':
   kontol()
