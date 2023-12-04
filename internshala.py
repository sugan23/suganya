# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:32:47 2023

@author: RAJESH KUMAR
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Create a Chrome WebDriver instance
driver = webdriver.Chrome() 

# Open Google
driver.get('https://www.google.com')

# Find the search bar using explicit wait
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    # Input "Internshala" into the search bar
    search_box.send_keys('Internshala')
    search_box.submit()

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.g'))
    )

    # Find all search results
    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    # Create and open a CSV file to write the results
    csv_file_path = 'C:/Users/RAJESH KUMAR/Documents/internshala_search_results.csv' 
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'URL', 'Description'])

        # Extract data for each search result
        for result in search_results:
            try:
                title = result.find_element(By.CSS_SELECTOR, 'h3').text
                url = result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                
                # Try to find the description, if not found, set it as an empty string
                description_elem = result.find_elements(By.CSS_SELECTOR, 'span.aCOpRe')
                description = description_elem[0].text if description_elem else ''
                
                # Write the data to the CSV file
                csv_writer.writerow([title, url, description])
            except Exception as e:
                print(f"Error processing search result: {e}")

finally:
    # Close the browser
    driver.quit()
