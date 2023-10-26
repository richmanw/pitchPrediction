from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def scrape_savant_profile(batter_name):

    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.get('https://baseballsavant.mlb.com/')

        wait = WebDriverWait(driver, 10)

        # Wait until "player-auto-complete loads"
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "player-auto-complete")))

        # Clear any existing text in the input field
        search_input.clear()
        # Input the desired batter's name
        search_input.send_keys(batter_name)
        # Send Return key
        search_input.send_keys(Keys.RETURN)

        statcast_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.statcast-group#statcastHitting')))

        raw_statcast_data = statcast_page.text

        print(raw_statcast_data)

    except NoSuchElementException as e:
        print("Search input field not found.")

    finally:
        # Close the WebDriver when done
        input("Press ENTER to close...")
        driver.quit()


def scrape_reference_profile(batter_name):
    # Provide the path to the Chrome WebDriver executable
    driver = webdriver.Chrome()
    driver.get('https://www.baseball-reference.com/')
