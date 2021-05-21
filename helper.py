import requests
from requests.models import requote_uri

def queryhandler(pincode):
    headers = {
        'authority': 'cdn-api.co-vin.in',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': 'W/^\\^8a6-9z/GOzR9hr6RUsnq88OszY1HPfs^\\^',
    }

    params = (
        ('pincode', f'{pincode}'),
        ('date', '21-05-2021'),
    )

    response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)
    return(response.json())
