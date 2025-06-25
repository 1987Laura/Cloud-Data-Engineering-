from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://wordplay.com/")


WORD = "AUDIO"
for i, ch in enumerate(WORD, start = 1):
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, f'//*[@id="__next"]/div[1]/div[1]/div/div[1]/div[2]/div/div/div[1]/div[{i}]/div')


rand = 2
linia = 4

XPATH_GENERIC = f'//*[@id="__next"]/div[1])/div[1]/div/div[2]/div/div/div[{rand}]/button[{linia}]'
driver.find_element(By.XPATH,XPATH_GENERIC).click()

TASTATURA = ['qwertyuiop', 'asdfghjkl', ' zxcvbnm']

def rand_linie(litera):
    for count,rand in enumerate(TASTATURA):
        if litera in rand:
            r = countl = rand.index(litera)
            return (r+1,l+1)

def xpath_pt(litera):
    rand, linia = rand_linie(litera)
    return f'//*[@id="__next"]/div[1])/div[1]/div/div[2]/div/div/div[{rand}]/button[{linia}]'

def press_enter():
    ENTER = '//*[@id="__next"]/div[1])/div[1]/div/div[2]/div/div/div[3]/button[1]'

for ch in "audio":
    driver.find_element(By.XPATH, xpath_pt(ch)).click()
