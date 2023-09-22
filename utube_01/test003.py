from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import time
import random

def test_visit_url_randomly():
    """
    Visits a URL randomly with a specified number of visits and random sleep durations.
    """
    try:
        # Set Firefox WebDriver to run in headless mode
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        for _ in range(1000):
            # Visit the URL
            driver.get("https://youtu.be/mek6Cur2-qU?si=p_Di1CGI91NhF6Ub")
            time.sleep(2)

            try:
                # Find and click the play button
                play_button = driver.find_element(By.XPATH, "//button[@class='ytp-play-button ytp-button']")
                play_button.click()
            except NoSuchElementException as e:
                print(f"Play button not found: {e}")

            # Generate a random sleep time
            sleep_time = random.randint(10, 35)

            # Sleep for the random duration
            time.sleep(sleep_time)

    except WebDriverException as e:
        print(f"Selenium WebDriver Exception: {e}")
    except Exception as e:
        print(f"An unexpected exception occurred: {e}")

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    test_visit_url_randomly()
