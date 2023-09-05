from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def scrapeProfile(pitcher_name):

    try:
        driver = webdriver.Chrome()

        driver.get("https://baseballsavant.mlb.com/")

        # Find the search input field by ID
        search_input = driver.find_element(By.ID, "player-auto-complete")

        # Clear any existing value in the search input field
        search_input.clear()

        # Enter the batter's name into the search input field
        search_input.send_keys(pitcher_name)

        # Submit the search form (if necessary)
        search_input.send_keys(Keys.RETURN)

        # Additional code to handle the search results can be added here

    except NoSuchElementException as e:
        print("Search input field not found.")

    finally:
        # Close the browser
        input("Press ENTER to close...")
        driver.quit()
