from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CarListings import CarListings

from bs4 import BeautifulSoup
import os, time
from sys import platform
import time
import json
import math
import re

maindir = os.path.dirname(os.path.abspath(__file__))



def init_firefox(headless=False):
    opts = FirefoxOptions()
    if headless:
        opts.add_argument("--headless")
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--start-maximized")

    if platform == "win32":
        opts.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver_executable = os.path.join(maindir, 'geckodriver.exe')
    elif platform == "linux" or platform == "linux2":
        driver_executable = os.path.join(maindir, 'geckodriver')
    driver = webdriver.Firefox(options = opts, executable_path = driver_executable)
    return driver



def main(url_list):
    start_time = time.time()

    car_list = []
    for USER_URL in url_list:
        print("Loading Selenium (firefox)...")
        driver = init_firefox(headless=False)

        print("Loading cars.com URL...")
        driver.get(USER_URL)

        CURRENT_CLASS = "vehicle-details"

        # container = driver.find_element(By.XPATH, "search-page-list-container")
        # action = ActionChains(driver)
        # for i in range(12):
        #     action.move_to_element(container).perform()
        #     if i < 10:
        #         action.click(container).perform()
        #     action.send_keys(Keys.PAGE_DOWN).perform()
        #     time.sleep(0.5)
        entries = []
        timeout = 0
        while not entries:
            time.sleep(1)
            html = driver.execute_script("return document.documentElement.outerHTML")
            soup = BeautifulSoup(html, 'html.parser')
            entries = soup.find_all(attrs={"class": CURRENT_CLASS})
            timeout += 1
            if timeout > 10:
                print(f"Timeout reached. Ending program...")
                driver.close()
                break
        
        for entry in entries:
            cl = CarListings(str(entry))
            car_list.append(cl)

        driver.close()

    print(f"Success! Results found: {len(car_list)}")
    
    with open("listings.json", "w") as f:
        listing = 1
        car_dict = {}
        for car in car_list:
            car_dict[listing] = car.to_dict()
            listing += 1
        json.dump(car_dict, f, indent=4)

    # time taken to 2 decimal points
    total_time = round(time.time() - start_time, 2)
    print(f"Time taken: {total_time} seconds")

if __name__ == "__main__":
    # step 1: Go to cars.com
    # step 2: Set your search parameters
    # step 3: Copy the urls FOR EACH INDIVIDUAL PAGE and paste it here
    # aside: r"" (raw string) eliminates the need to escape the backslashes

    # example setup:
    # url1 = r"https://www.cars.com/shopping/results/?list_price_max=blahblahblah"
    # url2 = r""
    # url3 = r""
    # url4 = r""
    # ...
    # urls = [url1, url2, url3, url4, ...]
    # main(urls)

    url1 = r"https://www.cars.com/shopping/results/?list_price_max=&makes%5B%5D=&maximum_distance=20&models%5B%5D=&page=1&page_size=100&stock_type=cpo&zip=48377"
    urls = [url1]
    main(urls)