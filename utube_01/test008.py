from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException
import time
import random

from selenium.webdriver.common.by import By

def test_visit_url_randomly():
    """
    Visits a URL randomly with a specified number of visits and random sleep durations.

    :param url: The URL to visit.
    :param num_visits: The number of times to visit the URL.
    :param min_sleep: The minimum sleep duration in seconds.
    :param max_sleep: The maximum sleep duration in seconds.
    """
    try:
        for _ in range(10):
            # Create a new Firefox WebDriver instance for each iteration
            driver = webdriver.Firefox()

            # Visit the URL
            driver.get("https://youtu.be/MB9aQ6Hkoz0?si=rjxMDN-Ofcl2d9-o")
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

            # Quit the WebDriver for this iteration
            driver.quit()

    except WebDriverException as e:
        print(f"Selenium WebDriver Exception: {e}")
    except Exception as e:
        print(f"An unexpected exception occurred: {e}")

if __name__ == "__main__":
    test_visit_url_randomly()
