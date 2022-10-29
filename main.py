import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pyautogui
import time

k = 0

GGbet = "https://ggbet.name/ru/esports/match/iron-branch-vs-fnatic-rising-13-10"
Parimatch = "https://pari-match-betting.com/ru/events/iron-branch-fnatic-rising-9140660"


url = GGbet
url_2 = Parimatch

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
options.headless = True
driver = webdriver.Chrome(executable_path=r"C:\Program\Projects\. Learning\Parcing\Selenium learning\chromedriver.exe", options=options)
driver_2 = webdriver.Chrome(executable_path=r"C:\Program\Projects\. Learning\Parcing\Selenium learning\chromedriver.exe", options=options)

driver.get(url=url)
driver_2.get(url=url_2)

while k < 1:
    sleep(4)

    with open("selenium.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)


    with open("selenium.html", encoding="utf-8") as file2:
        scr = file2.read()


    soup = BeautifulSoup(scr, "lxml")

    data = soup.find_all("div", class_="odd__ellipsis___3b4Yk")


    first_bet = data[0].text

    second_bet = data[1].text

    with open("selenium_2.html", "w", encoding="utf-8") as file_2:
        file_2.write(driver_2.page_source)


    with open("selenium_2.html", encoding="utf-8") as file2_2:
        scr_2 = file2_2.read()


    soup_2 = BeautifulSoup(scr_2, "lxml")

    data_2 = soup_2.find_all("span", class_="EC_lf_EC_ll")


    first_bet_2 = data_2[0].text

    second_bet_2 = data_2[1].text


    bet = []
    bet_sum_1_end = 0
    bet_sum_2_end = 0


    if first_bet > first_bet_2:
        bet_1 = first_bet
        bet_2 = second_bet_2
        bet.append(1)
        bet.append(2)
    else:
        bet_1 = first_bet_2
        bet_2 = second_bet
        bet.append(2)
        bet.append(1)


    def calculating(bet_1, bet_2):
        bal = 50

        global bet_sum_1_end
        global bet_sum_2_end

        bet_sum_1_start = 1/float(bet_1)/100*10000

        bet_sum_2_start = 1/float(bet_2)/100*10000

        bet_sum_1_end = float(f"{bet_sum_1_start/2:.1f}")

        bet_sum_2_end = float(f"{bet_sum_2_start/2:.1f}")

        success = bal - (bet_sum_1_end + bet_sum_2_end)
        return success

    success = calculating(bet_1, bet_2)