import time

from RPA.Browser.Selenium import Selenium

from functions import execution


class WebmotorsScrapper:

    def __init__(self):
        self.driver = Selenium()

    def access_site(self):
        self.driver.open_available_browser("https://www.google.com.br/")
        self.driver.delete_all_cookies()
        input_field = "css:input"
        self.driver.input_text(input_field, 'webmotors')
        self.driver.press_keys(input_field, "ENTER")

        time.sleep(5)

        self.driver.click_link("partial link:Webmotors")
        time.sleep(5)

        if self.driver.does_page_contain_button('xpath://*[@id="root"]/div[3]/div[2]/button'):
            self.driver.click_button('xpath://*[@id="root"]/div[3]/div[2]/button')
        time.sleep(5)

    def get_brands(self):
        self.driver.open_available_browser(self.url)
        time.sleep(5)
        self.driver.find_element('link:Ok').click()
        time.sleep(5)
        self.driver.find_element('xpath://*[@id="root"]/main/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/form/div['
                                 '5]/div[3]').click()
        time.sleep(5)

    def get_models_by_brand(self, brand):
        pass


def main():
    scrap = WebmotorsScrapper()
    scrap.access_site()


if __name__ == "__main__":
    main()
