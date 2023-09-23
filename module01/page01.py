from selenium.webdriver.common.by import By


class Page:
    def __init__(self,driver):
        self.driver=driver
    def click_shorts_button(self):
        play_button = self.driver.find_element(By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")
        play_button.click()