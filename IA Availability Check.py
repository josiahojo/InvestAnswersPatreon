from bs4.builder import TreeBuilderRegistry
import requests
from bs4 import BeautifulSoup
import webbrowser
import smtplib
import time

URL = 'https://www.patreon.com/InvestAnswers/membership'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

a = 0

def check_availability():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    script_list = soup.find_all('script')

    data = script_list[14].get_text()
    data_split = data.split('\n')

    matchers = ['patron_amount_cents','remaining']
    matching = [s for s in data_split if any(xs in s for xs in matchers)]


    if '"remaining": 0' in matching[3]:
        print("Altruist Subscription Not Available" + "\n")
    else:
        print("Altruist Subscription Available!!!" + "\n")
        webbrowser.open('https://www.patreon.com/InvestAnswers/membership')
        send_mail()

    if '"remaining": 0' in matching[5]:
        print("Professional Subscription Not Available" + "\n")
    else:
        print("Professional Subscription Available!!!" + "\n")
        webbrowser.open('https://www.patreon.com/InvestAnswers/membership')
        send_mail()

    if '"remaining": 0' in matching[7]:
        print("Investor Subscription Not Available" + "\n")
    else:
        print("Investor Subscription Available!!!" + "\n")
        webbrowser.open('https://www.patreon.com/InvestAnswers/membership')
        send_mail()

    if '"remaining": 0' in matching[9]:
        print("Capitalist Subscription Not Available" + "\n")
    else:
        print("Capitalist Subscription Available!!!" + "\n")
        webbrowser.open('https://www.patreon.com/InvestAnswers/membership')
        send_mail()
        

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo

    #Add email address and password

    server.login('my_email_address@domain.com', 'my_password')

    subject = 'InvestAnswers Partreon Available'
    body = 'Check out the link https://www.patreon.com/InvestAnswers/membership'

    msg = f"Subject: {subject}\n\n{body}"

    #Enter the "FROM:" email address then the "TO:" email address
   
    server.sendmail(
        'your_email_address@domain.com',
        'phone_number_email_address@domain.com', 
        msg
    )
    print('EMAIL/TEXT HAS BEEN SENT!')
    exit()

while(True):
    check_availability()
    a+=1
    print("Try Number: ", a)
    print("************************")
    time.sleep(15)
