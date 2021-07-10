import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT_URL = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5XSG8Z/ref=sr_1_2_sspa?dchild=1&keywords=macbook&qid=1625915215&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSDU3VkJVSzQ2VTc4JmVuY3J5cHRlZElkPUEwNTc0NTE5MTY0Mlg1NDY5VVYxJmVuY3J5cHRlZEFkSWQ9QTA3MDY2NDYzNVo4V1k3SkpDSFAxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url=PRODUCT_URL, headers=headers)
website_code = response.text

soup = BeautifulSoup(website_code, "lxml")
price_with_tag = soup.find(name="span", id="priceblock_ourprice")
price_string = price_with_tag.getText()
price_without_symbol = price_string.split()
final_price = price_without_symbol[1]
new_final_price = final_price.replace(",", "")
floating_new_final_price = float(new_final_price)

email = "user_email"
password = "user_password"
receiving_email = "ayushgiri56@gmail.com"

if floating_new_final_price < 85000.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=receiving_email, msg=f"Subject:Price_drop\n\nThe new price now is {floating_new_final_price}")




