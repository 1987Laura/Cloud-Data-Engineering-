from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


def close_commercial_popup(driver):
    try:
        time.sleep(1.5) 
        driver.find_element(By.XPATH, '//button[contains(@class, "close")]').click()
        print("pop-up closed")
    except NoSuchElementException:
        print("No pop-up")
    except Exception as e:
        print(f" Error handling pop-up: {e}")


driver = webdriver.Chrome()
driver.get("https://icanhazdadjoke.com")

#inchide pop up cu cookies
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]/p').click()

with open('jokes.txt','a') as fwriter:
    for i in range (1,4):
        try:
            # inchide pop-up daca apare
            close_commercial_popup(driver)

            # Extract and write joke
            joke = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div/p').text
            print(f" Joke {i+1}: {joke}")
            fwriter.write(joke + "\n\n")

            # Go to next joke
            next_btn = driver.find_element(By.XPATH, '/html/body/section/div/div[1]/div[2]/a/span[2]')
            next_btn.click()

            time.sleep(1.5)  # Small delay to allow next page to load
        except Exception as e:
            print(f"Error at joke {i+1}: {e}")
            break
