from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-notifications")
chromeOptions.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://www.visualcapitalist.com/the-average-u-s-tariff-rate-since-1890/")
time.sleep(15)

view = (driver.find_element(By.XPATH, '//*[@id="dt-length-0"]'))
view.click()

for i in range(3):
    view.send_keys(Keys.ARROW_DOWN)

view.click()

with open("TariffRates.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Tariff Rate"])

for i in range(1, 126):
    if i == 101:
        page = driver.find_element(By.XPATH, '//*[@id="tablepress-5523_wrapper"]/div[3]/div[2]/div/nav/button[3]')
        page.click()
    if i >= 101:
        n = i - 100
        year = driver.find_element(By.XPATH, f'//*[@id="tablepress-5523"]/tbody/tr[{n}]/td[1]').text.strip()
        tariffRate = driver.find_element(By.XPATH, f'//*[@id="tablepress-5523"]/tbody/tr[{n}]/td[2]').text.strip()

    else:
        year = driver.find_element(By.XPATH, f'//*[@id="tablepress-5523"]/tbody/tr[{i}]/td[1]').text.strip()
        tariffRate = driver.find_element(By.XPATH, f'//*[@id="tablepress-5523"]/tbody/tr[{i}]/td[2]').text.strip()

    print(year, tariffRate)

    with open("TariffRates.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([year, tariffRate])