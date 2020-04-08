from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time

def scrapeMediamarkt():
    driver.get(mediamarkt)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    notAvailable = soup.findAll("div", attrs={'class':'PriceAndEnergyDetialsstyled__StyledProductNotAvailable-sc-8r5sng-0'})
    if (notAvailable):
        print(" {0} | Switch not available at Mediamarkt".format(datetime.now()))
    else:
        print(" {0} | SWITCH AVAILABLE AT Mediamarkt!!".format(datetime.now()))

def scrapeSaturn():
    driver.get(saturn)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    notAvailable = soup.findAll("span", attrs={'class':'snk_avail_clr01'})
    if (not notAvailable):
        print(" {0} | Switch not available at Saturn".format(datetime.now()))
    else:
        print(" {0} | SWITCH AVAILABLE AT SATURN!!".format(datetime.now()))

saturn = "https://www.saturn.de/de/product/_nintendo-switch-animal-crossing-new-horizons-edition-2633118.html"
mediamarkt = "https://www.mediamarkt.de/de/product/_switch-animal-crossing-new-horizons-edition-nintendo-switch-konsolen-2633118.html"


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("/usr/lib/chromium/chromedriver", options=options)


while True:
    scrapeMediamarkt()
    scrapeSaturn()
    print("---------------------------------------")
    time.sleep(60)



