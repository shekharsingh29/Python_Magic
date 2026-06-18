import re
from bs4 import BeautifulSoup
import requests
import smtplib, ssl
import os
from dotenv import dotenv_values


# get top 100 songs
def get_amazon_price(amazon_link):
   
    print(f"Amazon URL: {amazon_link}")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", 
        "Accept-Encoding": "gzip, deflate, br, zstd", 
        "Accept-Language": "en-US,en;q=0.5", 
        "Priority": "u=0, i", 
        "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"", 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": "\"Windows\"", 
        "Sec-Fetch-Dest": "document", 
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-Site": "cross-site", 
        "Sec-Fetch-User": "?1", 
        "Sec-Gpc": "1", 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    page = requests.get(amazon_link, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="a-price-whole")
    curreny = soup.find(class_="a-price-symbol")
    # music_list = results.find_all("h3",id="title-of-a-story", class_="a-no-trucate")
    print( curreny.text + results.text.split('.')[0])

    return curreny.text, results.text

def send_alert(price, amazon_link):
    
    # Configuration
    config = dotenv_values(".env")
    print(f"config {config}")
    config = list(config.items())
    print(f"config After {config}")

    sender_email = config[1][1]
    sender_password = config[2][1]
    context = ssl.create_default_context()

    # Plain text content
    message = f"""\
    Hi,
    The price is below 100 for your watchlist {amazon_link}. Please go ahead and buy it
    """

    try:
        server = smtplib.SMTP(config[0][1], 587)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, "")
        server.sendmail(sender_email, sender_email, message)
        print("Email delivered")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


if __name__ == "__main__":
    print("___________________________________________________ AMAZON PRIZE  ____________________________________________________________")
    amazon_link = "https://appbrewery.github.io/instant_pot/"
    currency, price = get_amazon_price(amazon_link)

    if float(price) < 100:
        send_alert(price, amazon_link)

