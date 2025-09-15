from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Install and set the driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the page
driver.get("https://es.openfoodfacts.org/")

# Wait 5 seconds
time.sleep(4)

# Product info
name_products = []
nutri_score = []
nova_score = []
green_score = []

product_contents = driver.find_elements(By.CLASS_NAME,"list_product_content")

for p_c in product_contents:

    # Name of the product
    name_products.append(p_c.find_element(By.CLASS_NAME,"list_product_name").text)

    quality_infos = p_c.find_elements(By.CLASS_NAME,"list_product_icons")
    
    nu_score = (quality_infos[0].get_attribute("title"))
    n_score = quality_infos[1].get_attribute("title")
    g_score = quality_infos[2].get_attribute("title")


# Close the browser
driver.quit()