sgk_link = "https://www.sgk.gov.tr/Istatistik/Aylik/42919466-593f-4600-937d-1f95c9e252e6/" 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get(sgk_link)

# Wait and select the statistic type
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'statisticType')))
dropdown = Select(driver.find_element(By.ID, 'statisticType'))
dropdown.select_by_value('1')

# Wait for the month dropdown to be populated
time.sleep(5)  # Adjust the sleep time as necessary

for year in range(2019, 2024):  # Loop through years 2019 to 2023
    # Select the year
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'year')))
    year_dropdown = Select(driver.find_element(By.ID, 'year'))
    year_dropdown.select_by_value(str(year))

    for month in range(1, 13):  # Loop through months 1 to 12
        try:
            # Wait for month dropdown to be populated
            time.sleep(5)  # Adjust as necessary

            # Select the month
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'month')))
            month_dropdown = Select(driver.find_element(By.ID, 'month'))
            month_dropdown.select_by_value(str(month))

            # Click the download button
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'istatistik-down')))
            download_button = driver.find_element(By.ID, 'istatistik-down')
            download_button.click()

            # Wait for the file to download before moving to the next month/year
            # Add appropriate delay or check for file download completion

        except (NoSuchElementException, TimeoutException):
            print(f"Data for {year}-{month} is not available. Moving to the next available month/year.")
            continue  # Skip the rest of the current loop iteration and proceed with the next month/year

        # Optional: Add a brief pause before the next iteration
        time.sleep(5)  # Adjust as necessary