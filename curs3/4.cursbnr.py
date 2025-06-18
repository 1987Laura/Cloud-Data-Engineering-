from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.cursbnr.ro"
driver = webdriver.Chrome()
driver.get(URL)

cookie_button_xpath = "/html/body/div[6]/div[2]/div[2]/div[2]/div[2]/button[1]/p"
driver.find_element(By.XPATH,cookie_button_xpath).click()


valoare_euro = '/html/body/div[3]/div[1]/div/main/div[2]/div[1]/ul/li[1]/div[1]/div[1]'

with open('curs_bnr.txt','a') as fwriter:
    fwriter.write(driver.find_element(By.XPATH,valoare_euro).text)
