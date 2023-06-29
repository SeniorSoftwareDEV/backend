from flask import request
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from api.config import app


@app.route("/activity/getsplithistory", methods=["POST"])
def get_splithistory():
    if (
        request.method == "POST"
        and "symbol" in request.form
    ):
        symbol = request.form["symbol"]
        url = f'https://www.stocksplithistory.com/?symbol={symbol}'
        print(url)
        options =  webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-application-cache')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--headless")

        s=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=options)
        print('Scraping start---')
        driver.get(url)
        table_element = driver.find_element(By.XPATH, '/html/body/center/div[4]/table[2]/tbody/tr/td[6]/table[1]')
        print(table_element)
        rows = table_element.find_elements(By.XPATH,'.//tbody/tr')
        rawArray= []
        i=0
        for row in rows:
            if i > 1:
                cells = row.find_elements(By.XPATH, './/td')
            else:
                i+=1
                continue
            j=0
            for cell in cells:
                rawArray.append(cell.text)
        print(rawArray)


        # split the even and odd values into separate lists
        even = []
        odd = []
        for i in range(len(rawArray)):
            if i % 2 == 0:
                even.append(rawArray[i])
            else:
                odd.append(rawArray[i])
        splitHistory = []
        for i in range(len(even)):
            obj = {"Date": even[i], "Ratio": odd[i]}
            splitHistory.append(obj)

        print('Scraping done')

        return splitHistory

