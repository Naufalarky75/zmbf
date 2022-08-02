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
reset = "[/]"
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
zxc = "fbkey"
ff = "fall"
xv = "xavier"

###----------[ APPEND AND MORE ]---------- ###
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
opt = []
idz = []
apk = []
files = []
id_groups = []
data = {}
ugent1, ugent2 = [],[]
datt = []
###----------[ CHECK STATUS SCRIPT ]---------- ###
try:
	info = ses.get("https://raw.githubusercontent.com/ReinXou/reinxou.github.io/main/info.txt").text
	if "maintenance" in info:
		prints(Panel(f"""{P2}Sorry, the script is currently under maintenance, please wait until it finishes updating. thanks you<3""",width=80,style=f"{color_table}"))
		sys.exit()
except requests.exceptions.ConnectionError:
	prints(Panel(f"""{P2}connection problem, please check your connection again""",width=80,style=f"{color_table}"))
	sys.exit()
	
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

###----------[ CLEAR TERMINAL ]---------- ###
def clear_screen():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

###----------[ DELETE LOGIN ]---------- ###
def delete():
	try:os.remove("data/token.txt")
	except:pass
	try:os.remove("data/cookie.txt")
	except:pass

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "good morning"
	elif 12 <= hours < 15:timenow = "good afternoon"
	elif 15 <= hours < 18:timenow = "good evening"
	else:timenow = "good night"
	return timenow

def menu_apikey():
	logo()
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. I have apikey and want to enter it
[{color_rich}02{P2}]. I don't have Apikey and want to buy 
[{color_rich}03{P2}]. I want to see the results crack""",width=80,padding=(0,15),style=f"{color_table}"))
	api = input(f" {N}input choice : ")
	if api in["1","01"]:
		prints(Panel(f"""{P2}enter the apikey you have, if not, please buy by selecting number 2""",width=80,style=f"{color_table}"))
		key = input(f" {N}input apikey : {H}")
		open("data/apikey.txt","w").write(key)
		menu()
	elif api in["2","02"]:
		os.system("xdg-open https://wa.me/6282329761867?text=assalamualaikum,+bang+saya+mau+beli+lisensi")
		sleep(2);menu_apikey()
	elif api in["3","03"]:
		Lain.see_results()

###----------[ LOGO ]---------- ###
def logo():
	clear_screen()
	prints(Panel(f"""{color_rich} ________   ___      ___  _______    _______  
("      "\ |"  \    /"  ||   _  "\  /"     "|  {M2}██████████████████████{reset}
 \___/   :) \   \  //   |(. |_)  :)(: ______)  {M2}██████████████████████{reset}
   /  ___/  /\\  \/.    ||:     \/  \/    |     {P2}██████████████████████{reset}
  //  \__  |: \.        |(|  _  \\  // ___)     {P2}██████████████████████{reset}
 (:   / "\ |.  \    /:  ||: |_)  :)(:  (      
  \_______)|___|\__/|___|(_______/  \__/      Made By {M2}Indonesia {P2}Coder""",title=f"{P2}{waktu()}",style=f"{color_table}"))

###----------[ MAIN MENU ]---------- ###
def menu():
	try:
		token = open("data/token.txt","r").read()
		cok = open("data/cookie.txt","r").read()
		cookie = {"cookie":cok}
		data = ses.get(f"https://graph.facebook.com/me?fields=name,id,birthday &access_token={token}",cookies=cookie).json()
		nama = data["name"]
		uid = data["id"]
		ttl = data["birthday"]
	except (FileNotFoundError,KeyError,IOError):
		delete()
		Login.login()
	logo()
	akmj = []
	email = "namamu@gmail.com"
	joined = "24 Maret 2022"
	expired = "24 Maret 2023"
	akmj.append(Panel(f"{P2}Nama : {nama} \nID : {uid} \nTgl Lahir : {ttl}",width=37,title=f"{P2}data account",style=f"{color_table}"))
	akmj.append(Panel(f"{P2}Email : {email} \nBergabung : {joined} \nKadaluwarsa : {expired}",width=37,title=f"{P2}data apikey",style=f"{color_table}"))
	console.print(Columns(akmj))

	prints(Panel(f"{P2}{IP}",padding=(0,30),title=f"{P2}IP",subtitle=f"{H2}{negara}",style=f"{color_table}"))
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. crack from search name v1 [{color_rich}09{P2}]. crack from group members
[{color_rich}02{P2}]. crack from search name v2 [{color_rich}10{P2}]. crack from post coments v1
[{color_rich}03{P2}]. crack from search name v3 [{color_rich}11{P2}]. crack from post coments v2
[{color_rich}04{P2}]. crack from random email   [{color_rich}12{P2}]. crack from messengers
[{color_rich}05{P2}]. crack from public friends [{color_rich}13{P2}]. crack from requests page
[{color_rich}06{P2}]. crack from multi target   [{color_rich}14{P2}]. crack friends from friends
[{color_rich}07{P2}]. crack from followers      [{color_rich}15{P2}]. crack friends from search
[{color_rich}08{P2}]. crack from all reactions  [{color_rich}16{P2}]. crack from multi files""",width=80,padding=(0,4),style=f"{color_table}"))
	prints(Panel(f"""{P2}type 'bot' for enter to bot menu or type 'more' for enter to more menu""",width=80,style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	if ask in["1","01"]:
		Dump.search_name_v1()
	elif ask in["2","02"]:
		Dump.search_name_v2()
	elif ask in["3","03"]:
		Dump.search_name_v3(cookie)
	elif ask in["4","04"]:
		Dump.random_email()
	elif ask in["5","05"]:
		Dump.public_friends(token,cookie)
	elif ask in["6","06"]:
		Dump.multi_target(token,cookie)
	elif ask in["7","07"]:
		Dump.followers(token,cookie)
	elif ask in["8","08"]:
		Dump.all_reactions(cookie)
	elif ask in["9","09"]:
		Dump.group_members(token,cookie)
	elif ask in["10"]:
		Dump.public_comments_v1(cookie)
	elif ask in["11"]:
		Dump.public_comments_v2()
	elif ask in["12"]:
		Dump.message(token,cookie)
	elif ask in["13"]:
		Dump.requests_page(cookie)
	elif ask in["14"]:
		Dump.friendsfromfriends(token,cookie)
	elif ask in["15"]:
		Dump.friends_from_search(token,cookie)
	elif ask in["16"]:
		Dump.multi_files()
	elif ask in["bot"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif ask in["more"]:
		more_menu()
	else:
		menu()
		
def bot_menu():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. bot share from version 1  [{color_rich}06{P2}]. bot reactions from home
[{color_rich}02{P2}]. bot share from version 2  [{color_rich}07{P2}]. bot reactions from machine
[{color_rich}03{P2}]. bot coment from version 1 [{color_rich}08{P2}]. bot accept friends list
[{color_rich}04{P2}]. bot coment from version 2 [{color_rich}09{P2}]. bot unfriend friends list
[{color_rich}05{P2}]. bot coment allpost profil [{color_rich}10{P2}]. bot follow from result ok""",width=80,padding=(0,4),style=f"{color_table}"))
	ask = input(f" {N}input choice : ")
	
###----------[ ANY MORE MENU AVAILABLE ]---------- ###
def more_menu():
	prints(Panel(f"""{P2}[{color_rich}01{P2}]. see all results cracks    [{color_rich}06{P2}]. settings your user agent
[{color_rich}02{P2}]. checkpoint detector       [{color_rich}07{P2}]. change theme color
[{color_rich}03{P2}]. take id for target crack  [{color_rich}08{P2}]. cek update version now
[{color_rich}04{P2}]. dump id for output file   [{color_rich}09{P2}]. information tools & author
[{color_rich}05{P2}]. check information account [{color_rich}10{P2}]. logout (delete login)""",width=80,padding=(0,4),style=f"{color_table}"))
	tol = input(f" {N}input choice : ")
	if tol in["1","01"]:
		Lain.see_results()
	elif tol in["2","02"]:
		Lain.check_option()
	elif tol in["3","03"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["4","04"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["5","05"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["6","06"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["7","07"]:
		Lain.change_theme()
	elif tol in["8","08"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["9","09"]:
		prints(Panel(f"""{P2}feature is not available at this time. please wait for the update""",width=80,style=f"{color_table}"))
		exit()
	elif tol in["10"]:
		delete()
		prints(Panel(f"""{P2}successfully deleted token login info and cookies""",width=80,style=f"{color_table}"))
		exit()
	else:
		menu()