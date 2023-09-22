from selenium import webdriver
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
    # Create a Firefox WebDriver instance
    driver = webdriver.Firefox()
    for _ in range(1000):
        # Visit the URL
        driver.get("https://youtu.be/mek6Cur2-qU?si=p_Di1CGI91NhF6Ub")
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@class='ytp-play-button ytp-button']").click()

        # Generate a random sleep time
        sleep_time = random.randint(10, 35)

        # Sleep for the random duration
        time.sleep(sleep_time)
        driver.quit()








