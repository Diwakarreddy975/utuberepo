import random
import time
from selenium.webdriver.common.by import By
import page01
from conftest import read_config


class TestUtube:


    def test01(self):
        for _ in range(10):
            pom = page01.Page(self.driver)
            self.driver.get(read_config())
            time.sleep(2)
            pom.click_shorts_button()
            sleep_time = random.randint(10, 35)

            # Sleep for the random duration
            time.sleep(sleep_time)
            self.driver.quit()


    def test02(self, selenium_driver):
        for _ in range(10):
            pom = page01.Page(self.driver)
            self.driver.get(read_config())
            time.sleep(2)
            pom.click_shorts_button()
            sleep_time = random.randint(10, 35)

            # Sleep for the random duration
            time.sleep(sleep_time)
            self.driver.quit()


    def test03(self, selenium_driver):
        for _ in range(10):
            pom = page01.Page(self.driver)
            self.driver.get(read_config())
            time.sleep(2)
            pom.click_shorts_button()
            sleep_time = random.randint(10, 35)

            # Sleep for the random duration
            time.sleep(sleep_time)
            self.driver.quit()


    def test04(self, selenium_driver):
        for _ in range(10):
            pom = page01.Page(self.driver)
            self.driver.get(read_config())
            time.sleep(2)
            pom.click_shorts_button()
            sleep_time = random.randint(10, 35)

            # Sleep for the random duration
            time.sleep(sleep_time)
            self.driver.quit()


    def test05(self, selenium_driver):
        for _ in range(10):
            pom = page01.Page(self.driver)
            self.driver.get(read_config())
            time.sleep(2)
            pom.click_shorts_button()
            sleep_time = random.randint(10, 35)

            # Sleep for the random duration
            time.sleep(sleep_time)
            self.driver.quit()
