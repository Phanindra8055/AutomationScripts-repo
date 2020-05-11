from bs4 import BeautifulSoup  # Install bs4 (pip install bs4) for this to work
from time import sleep
import requests  # pip install requests
import smtplib  # pip install smtplib

url = "https://www.amazon.in/Lenovo-Ideapad-15-6-inch-Laptop-81MV0094IN/dp/B07S3WJ28F/ref=sr_1_1?dchild=1&fst=as%3Aoff&qid=1589139513&refinements=p_n_operating_system_browse-bin%3A1464493031&rnid=1464447031&s=computers&sr=1-1"  # Address of the product you want to track

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}  # search for 'My agent heads'

expecting_price = 25000  # Price at which you wanted to get notified.


def check_price():
    page = requests.get(url, headers=headers)

    # parsing the response from amazon
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:8].replace(',', ''))

    print(title)
    print(converted_price)

    if converted_price <= expecting_price:
        send_email()


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()  # Establishes connection
    server.starttls()  # Encrypts the connection
    server.ehlo()

    '''In order for this to work first enable 2-factor-autentication for you gmail account https://www.google.com/landing/2step/ 
    Then create a app password for your Gmail at https://myaccount.google.com/apppasswords?rapt=AEjHL4Ml-eVy2FhGl_KQ7us7_N7Iuj0JORmUTmh78VzvNobbydEE7-AxuWdGexSUzi4_EUVXvDCS4svVZACzVEzRC48a8cdDSg '''
    server.login('EMAIL_ADDRESS', 'APP_PASSWORD_FROM_GOOGLE')  # Replace 'EMAIL_ADDRESS' with your email address and replace 'APP_PASSWORD_FROM_GOOGLE' with you app password.

    subject = "Hey price fell down!"  # Keep whatever subject you want.
    body = "Check the Amazon link \n" + url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('FROM_EMAIL_ADDRESS', 'TO_EMAIL_ADDRESS',
                    msg)  # Replace FROM_EMAIL_ADDRESS with your (senders) email address and TO_EMAIL_ADDRESS with receivers email (Your email if you want your email to receive the mail).
    print("Hey Email has been sent!")  # confirmation that mail has been sent.

    server.quit()  # Quit the server at the end.


while True:
    '''Check the price for every 2 hours and sends an email if price fell down than you wanted'''
    check_price()
    sleep(2 * 60 * 60)
