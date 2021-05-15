from logging import error
from cowin_api import CoWinAPI
import telebot
import requests

browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

bot = telebot.TeleBot("1873127810:AAEKguCOmszM-yxSguts-TOB4eVXoZX2ul8")


#Bot handler for start and help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    if 1: #message.chat.id == 1265879761 or message.chat.id == 941874401 or message.chat.id == 887572477:
	    bot.reply_to(message, """Check Vaccination slots availability details quickly ,thanks for your interest in vacinnation drive.
Wear mask ,maintain social distance & wash hands regularly with soap
#IndiaFightsAgainstCorona

For those who still believe vaccines are not effective "Let's Live in peace rather resting in peace"
""")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    toprint = """Please Note: All data is fetched from the official cowin public api ,for more info and booking details visit https://www.cowin.gov.in/home
Slots available for you pincode :
"""
    if 1:#message.chat.id == 1265879761 or message.chat.id == 941874401 or message.chat.id == 887572477:
        if "/slot" in message.text:
            try:
                pin_code=(message.text).split(" ")[1]
            except :
                bot.reply_to(message,"""Something went wrong in split,make sure you have followed proper format and correct pin code
/slot pincode
example "/slot 560001" """)
                exit(0)
            #start colleting info
            try: 
                cowin = CoWinAPI()
                available_centers = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=560064&date=16-05-2021",browser_header) #cowin.get_availability_by_pincode(pin_code)
            except:
                bot.reply_to(message,"""Something went wrong in cowin requests ,make sure you have followed proper format and correct pin code
/slot pincode
example "/slot 560001" """)
                exit(0)
            try:
                for center in available_centers['centers']:
                    toprint = toprint + f"""
Center Name:{center['name']} - Center ID: {center['center_id']}
Address:{center['address']},{center['block_name']},{center['district_name']},{center['state_name']}-{center['pincode']}
Type:{center['fee_type']}
From:{center['from']} To:{center['to']} 
"""

                    for session in center['sessions']:
                        toprint = toprint + f"""
Vaccine Name: {session['vaccine']} 
Date:{session['date']}
Available Doeses:{session['available_capacity']}
Dose 1 Capacity:{session['available_capacity_dose1']}
Dose 2 Capacity:{session['available_capacity_dose2']}
Age Limit:{session['min_age_limit']}
slots:"""
                        for slot in session['slots']:
                            toprint=toprint+f""" {slot}
"""
                    bot.reply_to(message,toprint)
                    toprint=""" """
            except:
                bot.reply_to(message,"""Something went wrong ,make sure you have followed proper format and correct pin code
/slot pincode
example "/slot 560001" """)
                exit(0)



bot.polling()
