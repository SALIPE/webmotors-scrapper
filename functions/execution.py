import time
from RPA.Browser.Selenium import Selenium

def salve_bombon():
    scrapper = Selenium()

    scrapper.open_available_browser("https://www.google.com.br/")
    scrapper.delete_all_cookies()

    time.sleep(5)
    input_field = "xpath:/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    scrapper.input_text(input_field, 'Bombon é assim que tem que funfar o compilado?')
    # scrapper.press_keys(input_field, "ENTER")

    time.sleep(5)
    scrapper.close_browser()
    #
    # scrapper.click_link("partial link:Webmotors")
    #
    # time.sleep(5)