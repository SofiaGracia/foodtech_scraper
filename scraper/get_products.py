import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_products():

    # Install and set the driver automatically
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the page
    driver.get("https://es.openfoodfacts.org/")

    # Product info
    name_products = []
    nutri_score = []
    nova_score = []
    green_score = []

    info = [nutri_score, nova_score, green_score]

    # Wait for the elements to appear before scraping
    # Create a WebDriverWait object
    wait = WebDriverWait(driver=driver, timeout=10)
    product_contents = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"list_product_content")))

    for p_c in product_contents:

        # Name of the product
        name_products.append(p_c.find_element(By.CLASS_NAME,"list_product_name").text)

        quality_infos = p_c.find_elements(By.CLASS_NAME,"list_product_icons")

        # Manage the possible lack of info
        for i in range(3):
            if i < len(quality_infos):
                quality_info = quality_infos[i].get_attribute("title")
                info[i].append(quality_info if quality_info is not None else "N/A")
            else:
                # In case there's not enough icons
                info[i].append("N/A")

    # Close the browser
    driver.quit()

    data = zip(name_products, nutri_score, nova_score, green_score)

    return data
