from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram import filters
from datetime import datetime
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
import requests
from bs4 import BeautifulSoup

api_id = 27447876
api_hash = "ad57a4e2e56981f94c453275d80ef565"
proxy = {
	"scheme": "socks5",  # "socks4", "socks5" and "http" are supported
	"hostname": "127.0.0.1",
	"port": 1089,
}

app = Client("dani", api_id=api_id, api_hash=api_hash,
			 bot_token = "5844217170:AAEmHw3Qh__MO3NfUNL6kse2dPulxjABJQA",
			 proxy = proxy )
@app.on_message(filters.command(["start"]))
async def my_handler(client, message):
	await message.reply("Hello User, if you need help, use the /help command; otherwise welcome to the bot!",
		reply_markup=ReplyKeyboardMarkup(
                [
                    ["/help"], #1st row
					["date and time"], ["time and date"], #2nd
					["oghate shar-e"], ["اوقات شرعی"], #3rd row
					["azane sobh"], ["اذان صبح"], #4th
					["toloo"], ["طلوع"], #5th
					["azane zohr"], ["اذان ظهر"], #6th
					["ghoroob"], ["غروب"], #7th
					["azane maghreb"], ["اذان مغرب"], #8th
					["nime shabe shar-e"], ["نیمه شب شرعی"] #9th
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )			 
	)
	
@app.on_message(filters.command(["help"]))
async def my_handler(client, message):
	await message.reply("Use the pre-made keyboard to command the bot, or type the commands below: \n typing (date and time) returns the date first as Y-M-D and then time as H-M-S \n typing (time and date) returns the time first as H-M-S and then date as Y-M-D. \n for other commands type the keywords seen on the pre-made keyboard to get the functions.  ")

@app.on_message(filters.regex("date and time"))
async def my_handler(client, message):
	now = datetime.now()
	date_time1 = now.strftime("%y/%m/%d, %H:%M:%S")
	date_time2 = now.strftime("%H:%M:%S, %y/%m/%d")
	await message.reply(date_time1)

@app.on_message(filters.regex("time and date"))
async def my_handler(client, message):
	now = datetime.now()
	date_time1 = now.strftime("%y/%m/%d, %H:%M:%S")
	date_time2 = now.strftime("%H:%M:%S, %y/%m/%d")
	await message.reply(date_time2)

@app.on_message(filters.regex("oghate shar-e")) #english oghat
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azansobh = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'})[0].text #1
	toloo = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'})[0].text #2
	azanzohr = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'})[0].text #3
	ghoroob = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'})[0].text #4
	azanmaghreb = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'})[0].text #5
	nimeshabeshari = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'})[0].text #6
	stringofall = "Azane Sobh: \n" + azansobh + "\n Toloo Aftab: \n" + toloo + "\n Azane Zohr: \n" + azanzohr + "\n Ghoroob: \n" + ghoroob + "\n Azane Maghreb: \n" + azanmaghreb + "\n Nime Shabe Shar-e \n" + nimeshabeshari
	await message.reply(stringofall)

@app.on_message(filters.regex("اوقات شرعی")) #farsi oghat
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azansobh = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'})[0].text #1
	toloo = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'})[0].text #2
	azanzohr = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'})[0].text #3
	ghoroob = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'})[0].text #4
	azanmaghreb = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'})[0].text #5
	nimeshabeshari = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'})[0].text #6
	stringofall = "اذان صبح: \n" + azansobh + "\n طلوع آفتاب: \n" + toloo + "\n اذان ظهر: \n" + azanzohr + "\n غروب: \n" + ghoroob + "\n اذان مغرب: \n" + azanmaghreb + "\n نیمه شب شرعی: \n" + nimeshabeshari
	await message.reply(stringofall)




@app.on_message(filters.regex("azane sobh")) #english sobh
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azansobh = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'})[0].text
	string1 = "Azane Sobh: \n" + azansobh
	await message.reply(string1)

@app.on_message(filters.regex("اذان صبح")) #farsi sobh
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azansobh = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'})[0].text
	string1 = "اذان صبح: \n" + azansobh
	await message.reply(string1)






@app.on_message(filters.regex("toloo")) #english toloo
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	toloo = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'})[0].text
	string = "Toloo Aftab: \n" + toloo
	await message.reply(string)

@app.on_message(filters.regex("طلوع")) #farsi toloo
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	toloo = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'})[0].text
	string = "طلوع آفتاب: \n" + toloo
	await message.reply(string)





@app.on_message(filters.regex("azane zohr")) #english zohr
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azanzohr = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'})[0].text		
	string = "Azane Zohr: \n" + azanzohr
	await message.reply(string)

@app.on_message(filters.regex("اذان ظهر")) #farsi zohr
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azanzohr = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'})[0].text		
	string = "اذان ظهر: \n" + azanzohr
	await message.reply(string)




@app.on_message(filters.regex("ghoroob")) #english ghoroob
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	ghoroob = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'})[0].text		
	string = "Ghoroobe Aftab: \n" + ghoroob
	await message.reply(string)

@app.on_message(filters.regex("غروب")) #farsi ghoroob
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	ghoroob = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'})[0].text		
	string = "غروب آفتاب: \n" + ghoroob
	await message.reply(string)



@app.on_message(filters.regex("azane maghreb")) #english azan maghreb
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azanmaghreb = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'})[0].text		
	string = "Azane Maghreb: \n" + azanmaghreb
	await message.reply(string)

@app.on_message(filters.regex("اذان مغرب")) #farsi azan maghreb
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	azanmaghreb = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'})[0].text		
	string = "اذان مغرب: \n" + azanmaghreb
	await message.reply(string)




@app.on_message(filters.regex("nime shabe shar-e")) #english nime shari
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	nimeshabeshari = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'})[0].text		
	string = "Nime Shabe Shar-e: \n" + nimeshabeshari
	await message.reply(string)


@app.on_message(filters.regex("نیمه شب شرعی")) #farsi nime shari
async def my_handler(client, message):
	page = requests.get('https://www.time.ir/')
	soup = BeautifulSoup(page.text, 'html.parser')
	nimeshabeshari = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'})[0].text		
	string = "نیمه شب شرعی: \n" + nimeshabeshari
	await message.reply(string)

app.run()
