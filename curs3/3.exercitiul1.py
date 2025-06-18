from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get("https://link-academy.com")


COOKIE_BUTTON_ID = "politikaOK"
cookie_button = driver.find_element( By.ID, COOKIE_BUTTON_ID)
cookie_button.click()




programe_XPATH = '//*[@id="navLeft"]/ul/li[2]/a'
driver.find_element(By.XPATH, programe_XPATH).click()


driver.find_element(By.ID, "zatvori").click()


python_XPATH = '//*[@id="sidebarNav"]/div/div[2]/a[1]'
driver.find_element(By.XPATH, python_XPATH).click()

intro_to_python_XPATH = '//*[@id="content"]/table[1]/tbody/tr[2]/td[3]/a'
driver.find_element(By.XPATH, intro_to_python_XPATH).click()


