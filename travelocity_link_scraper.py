import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://www.travelocity.com/Hotel-Search?destination=San%20Francisco%20%28and%20vicinity%29%2C%20California%2C%20United%20States%20of%20America&regionId=178305&latLong=37.7874%2C-122.4082&flexibility=0_DAY&d1=2024-05-08&startDate=2024-05-08&d2=2024-05-22&endDate=2024-05-22&adults=2&rooms=1&theme=&userIntent=&semdtl=&useRewards=false&sort=RECOMMENDED'

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()

time.sleep(4)

while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        show_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show more')]")
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(show_more_button).perform()
        time.sleep(2)
    except NoSuchElementException:
        print("All results are loaded.")
        break


page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

links = soup.find_all('a', class_='uitk-card-link')

with open('travelocity_links.txt', 'a') as links_file:
    for link in links:
        links_file.write(f"https://www.travelocity.com{link.get('href')}\n")

driver.quit()
