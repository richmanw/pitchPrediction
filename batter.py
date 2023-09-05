from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def scrapeProfile(batter_name):

    try:
        driver = webdriver.Chrome()

        driver.get("https://baseballsavant.mlb.com/")

        # Find the search input field by ID
        search_input = driver.find_element(By.ID, "player-auto-complete")

        # Clear any existing value in the search input field
        search_input.clear()

        # Enter the batter's name into the search input field
        search_input.send_keys(batter_name)

        # Submit the search form
        search_input.send_keys(Keys.RETURN)
        print("Searching...")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "players-name")))

        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Wait for the body content to load inside the iframe
        WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "article-template")))

        # Get the body content
        body_content = driver.find_element(By.TAG_NAME, "article-template").text
        print(body_content)
        '''
        elements = driver.find_element_by_xpath('//td[@class="th-component-header align-left header table-static-column tablesorter-header tablesorter-headerUnSorted"]')
        element_list = []

        for element in elements:
            element_list.append(element)
            
        print(element_list)
        # Additional code to handle the search results can be added here
        iframe_locator = (By.TAG_NAME, "iframe")
        WebDriverWait(driver, 10).until(EC.precense_of_element_located(iframe_locator))

        iframe = driver.find_element(*iframe_locator)
        driver.switch_to(iframe)

        body_content = driver.find_element(By.TAG_NAME, "article-template").text
        print(body_content)
        '''
    except NoSuchElementException as e:
        print("Search input field not found.")

    finally:
        # Close the browser
        input("Press ENTER to close...")
        driver.quit()

