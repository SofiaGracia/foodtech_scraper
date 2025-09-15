from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import os

# Create dir data for csv
os.makedirs("data", exist_ok=True)

# Install and set the driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the page
driver.get("https://es.openfoodfacts.org/")

# Wait 5 seconds
time.sleep(2)

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

    # Manage the possible lack of info


    
    nutri_score.append(quality_infos[0].get_attribute("title"))
    nova_score.append(quality_infos[1].get_attribute("title"))
    green_score.append(quality_infos[2].get_attribute("title"))


# Close the browser
driver.quit()

data = zip(name_products, nutri_score, nova_score, green_score)

with open('data/first_fifty.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre del producto", "Nutri-Score", "Nova-Score", "Green-Score"])
    writer.writerows(data)