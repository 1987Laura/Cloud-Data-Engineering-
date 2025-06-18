from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://olx.ro")

time.sleep(3)
COOKIE_BUTTON_ID = "onetrust-accept-btn-handler"
cookie_button = driver.find_element( By.ID, COOKIE_BUTTON_ID)
cookie_button.click()

input()
driver.quit()