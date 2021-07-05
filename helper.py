import requests
from datetime import date

today = date.today()
print(f"{today.day}-{today.month}-{today.year}")

def queryhandler(pincode):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0)' #User agent required in the header for public api to work.
}
   
    params = (
        ('pincode', f'{pincode}'),
        ('date', f"{today.day}-{today.month}-{today.year}"),
    )

    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)
    return(response.json())
