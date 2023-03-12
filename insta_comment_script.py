import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


def main():

    arroba_list = pd.read_excel("arrobas.xlsx")
    browser = webdriver.Chrome()

    site_url = "https://www.instagram.com/login"
    browser.get(site_url)

    try:
        WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

        username_input = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_btn = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

        username_input.send_keys("falacmgleilei")
        password_input.send_keys("salipegay123")

        login_btn.click()
        time.sleep(5)

        browser.get("https://www.instagram.com/p/CgM9u-QAR-l/?utm_source=ig_web_copy_link")
        time.sleep(3)

        for name in arroba_list["arrobas"]:
            print(name)
            time.sleep(15)
            try:
                comment_area = browser.find_element(By.TAG_NAME, 'textarea')
                comment_area.click()
                comment_area.clear()
                comment_area.send_keys(name)
            except StaleElementReferenceException:
                comment_area1 = browser.find_element(By.TAG_NAME, 'textarea')
                comment_area1.click()
                comment_area1.clear()
                comment_area1.send_keys(name)

            form = browser.find_element(By.TAG_NAME, 'form')
            form.submit()

    except TimeoutException:
        print("Loading took too much time!")
    browser.close()


if __name__ == "__main__":
    main()
