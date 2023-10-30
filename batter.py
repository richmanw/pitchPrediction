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

        statcast_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.article-template')))
        raw_statcast_data = statcast_page.text

        run_values_by_pitch_type_numbers(raw_statcast_data)

    except NoSuchElementException as e:
        print("Search input field not found.")


# Accessing Values needed within Run Values by Pitch Type
def run_values_by_pitch_type_numbers(raw_statcast_data):
    target_string = "Run Values by Pitch Type"
    ending_string = "! Note: Years are in reverse order."
    raw_statcast_data = raw_statcast_data.split()
    current_word_index = 0
    target_string_final_index = 0
    ending_string_starting_index = 0

    current_word_index_hit = False
    while current_word_index < len(raw_statcast_data):

        if ' '.join(raw_statcast_data[current_word_index - 5:current_word_index]) == target_string:
            target_string_final_index = current_word_index
            current_word_index_hit = True

        if current_word_index_hit:
            if ' '. join(raw_statcast_data[current_word_index - 7:current_word_index]) == ending_string:
                ending_string_starting_index = current_word_index
                break

        current_word_index += 1

    run_value_numbers = raw_statcast_data[target_string_final_index: ending_string_starting_index]
    build_run_value_table(run_value_numbers)


def build_run_value_table(run_value_numbers):
    # Need to break up list into rows of 17
    sublist_size = 17
    current_position = 0
    tables = []
    table = []
    i = 0

    while i < len(run_value_numbers):
        if run_value_numbers[i] == "Pitch":
            table.append("Pitch Type")
            i += 2

        if run_value_numbers[i] == "Run":
            table.append("Run Value")
            i += 2

        if run_value_numbers[i] == "PutAway":
            table.append("PutAway %")
            i += 2

        if run_value_numbers[i] == "Hard":
            table.append("Hard Hit %")
            i += 3

        if run_value_numbers[i] != "Team":
            table.append(run_value_numbers[i])

        current_position += 1
        i += 1

        if current_position == sublist_size:
            tables.append(table)
            table = []
            current_position = 0

    for z, pitch_type in enumerate(tables, 1):
        print(f"Pitch Type {z}: {pitch_type} ")


def scrape_reference_profile(batter_name):
    # Provide the path to the Chrome WebDriver executable
    driver = webdriver.Chrome()
    driver.get('https://www.baseball-reference.com/')
