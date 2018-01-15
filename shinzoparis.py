import requests
from random import getrandbits
from time import sleep
from bs4 import BeautifulSoup

main_url = 'https://raffle.shinzo.paris/levis-x-air-jordan-4-denim/'
form_url = 'https://raffle.shinzo.paris/levis-x-air-jordan-4-denim/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

session = requests.Session()
session.headers.update(headers)

# CHANGE the fields as the comments say
def main(limit):
    sitekey = '6LczOjoUAAAAABEfbqdtD11pFD5cZ0n5nhz89nxI' #sitekey
    
    api_key = '' # COPY YOUR 2CAPTCHA KEY HERE.
    
    for i in range(1, limit):
        cap_id = session.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(api_key, sitekey, main_url)).text.split('|')[1]
        cap_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, cap_id)).text
        while 'CAPCHA_NOT_READY' in cap_answer:
            print('Waiting for captcha. Sleeping!')
            sleep(3)
            cap_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, cap_id)).text
        return_cap = cap_answer.split('|')[1]
        
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        
        payload = {
		'_wpcf7'				: '5', #dont change
		'_wpcf7_version'		: '4.9.1', #dont change
		'_wpcf7_locale'			: 'fr_FR', #dont change
		'_wpcf7_unit_tag'		: 'wpcf7-f5-p2-o1', #dont change
		'_wpcf7_container_post' : '2', #dont change
		'lang'					: "fr", #dont change
        'your-firstname'		: '', #Enter first name
        'your-name'				: '', #Enter last name
        'your-email'			: email, #DONT CHANGE
        'your-tel'				: '', #ENTER PHONE NUMBER
        'size'					: '', #Edit for what size you want
        'opt-in[]'				: '1', #DONT CHANGE  
		'accept'				: '1', #DONT CHANGE
		'g-recaptcha-response'	: return_cap

        }
        resp = requests.post(form_url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit,))


if __name__ == "__main__":
    main(100000)