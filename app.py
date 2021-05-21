import requests
import telebot
from helper import queryhandler



bot = telebot.TeleBot("1829549895:AAETrgNwUl-R1p4bQX3Pg4v9M-4wZLld3jU")


#Bot handler for start and help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    if 1:#message.chat.id == -1001416258735 or message.chat.id == 941874401 or message.chat.id == 887572477:
        bot.send_photo(message.chat.id,"https://telegra.ph/file/101ee79716b7af4db8ecb.jpg","""Welcome to Covid-19 Vaccination Slots Finder Bot 
How to use?
/slot pincode

ecample:
/slot 560001

For those who still believe vaccines are not effective "Let's Live in peace rather resting in peace""")
	    
    else:
        bot.reply_to(message,"Sorry bot is in beta mode ,so will only work in https://t.me/joinchat/kWRg_grIcAE5NzY1")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    toprint = """Please Note: All data is fetched from the official cowin public api ,for more info and booking details visit https://www.cowin.gov.in/home
Slots available for you pincode :
"""
    if 1:#message.chat.id == -1001416258735 or message.chat.id == 941874401 or message.chat.id == 887572477:
        if "/slot" in message.text:
            try:
                pin_code=(message.text).split(" ")[1]
            except :
                bot.reply_to(message,"""Something went wrong ,make sure you have followed proper format and correct pin code
/slot pincode
example "/slot 560001" """)
                exit(0)
                
            #start colleting info
            try: 
                #cowin = CoWinAPI()
                #available_centers = cowin.get_availability_by_pincode(pin_code)
                available_centers = queryhandler(pin_code)

            except:
                bot.reply_to(message,"""Something went wrong ,make sure you have followed proper format and correct pin code
/slot pincode
example "/slot 560001" """)
                exit(0)
            try:
                for center in available_centers['centers']:
                    toprint = toprint + f"""
*Center Name:{center['name']} - Center ID: {center['center_id']}*
_Address:{center['address']},{center['block_name']},{center['district_name']},{center['state_name']}-{center['pincode']}_
Type:{center['fee_type']}
_From:{center['from']} To:{center['to']}_
"""

                    for session in center['sessions']:
                        toprint = toprint + f"""
*Vaccine Name: {session['vaccine']}*
*Date:{session['date']}*
Available Doeses:{session['available_capacity']}
Dose 1 Capacity:{session['available_capacity_dose1']}
Dose 2 Capacity:{session['available_capacity_dose2']}
*Age Limit:{session['min_age_limit']}*
slots:"""
                        for slot in session['slots']:
                            toprint=toprint+f""" *{slot}*
"""
                    bot.reply_to(message,toprint,parse_mode="Markdown")
                    toprint=""" """
            except:
                bot.reply_to(message,"""Something went wrong ,make sure you have followed proper format and correct pin code
/slot pincode
example "/slot 560001" """)
                



bot.polling()