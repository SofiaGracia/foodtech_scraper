from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
from get_products import get_products as gp

# Create dir data for csv
os.makedirs("data", exist_ok=True)

data = gp()

with open('data/first_fifty.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre del producto", "Nutri-Score", "Nova-Score", "Green-Score"])
    writer.writerows(data)