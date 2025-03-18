import csv
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# Load the base URL to establish a session
driver.get("https://www.potterybarn.com/")
print("Loaded the base URL to establish a session.")

# Load cookies from cookies.txt file
try:
    with open('config/cookies.txt', 'r') as file:
        cookies = json.load(file)
    print("Cookies loaded successfully from 'cookies.txt'.")
except FileNotFoundError:
    print("Error: 'cookies.txt' file not found. Please ensure the file exists in the 'config' folder.")
    driver.quit()
    exit()

# Add cookies to the browser session
for cookie in cookies:
    if cookie.get('sameSite') is None:
        cookie['sameSite'] = 'Lax'
    for key in ['expiry', 'expires']:
        if key in cookie:
            del cookie[key]
    try:
        driver.add_cookie(cookie)
        print(f"Cookie added: {cookie['name']}")
    except Exception as e:
        print(f"Error adding cookie '{cookie['name']}': {e}")

# Navigate to the product listing page
product_listing_url = "https://www.potterybarn.com/shop/furniture/sofa/?cm_type=gnav&originsc=furniture&tabnav=non-mobiletabnav"
driver.get(product_listing_url)
print("Navigated to the product listing page.")
time.sleep(20)

# Extract product URLs
try:
    grid_items = driver.find_elements(By.CLASS_NAME, "grid-item")
    product_urls = {
        f"product_{index + 1}": item.find_element(By.TAG_NAME, "a").get_attribute("href")
        for index, item in enumerate(grid_items)
    }
    print(f"Found {len(product_urls)} product URLs.")
except NoSuchElementException:
    print("Error: Could not find product grid items. Check the page structure.")
    driver.quit()
    exit()

# Save product URLs to a JSON file
try:
    with open("data/product_urls.json", "w", encoding="utf-8") as file:
        json.dump(product_urls, file, indent=4)
    print("Product URLs saved to 'data/product_urls.json'.")
except Exception as e:
    print(f"Error saving product URLs: {e}")

# Extract product details
product_details = []
for product_name, url in product_urls.items():
    driver.get(url)
    time.sleep(3)
    try:
        title = driver.find_element(By.CSS_SELECTOR, "h1.heading-title-pip").text
        price = driver.find_element(By.CSS_SELECTOR, "li.sale-price span.amount").text
        image_url = driver.find_element(By.CSS_SELECTOR, "div.justify-center.relative img").get_attribute("src")
        description = driver.find_element(By.CSS_SELECTOR, "div.w-full .column-left, div.w-full .column-right").text

        product_details.append({
            "Name": title,
            "Price": price,
            "Image URL": image_url,
            "Description": description
        })
        print(f"Extracted details for: {title}")
    except NoSuchElementException as e:
        print(f"Error extracting details for {product_name}: {e}")

# Save product details to a CSV file
try:
    with open("data/product_details.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Price", "Image URL", "Description"])
        writer.writeheader()
        writer.writerows(product_details)
    print("Product details saved to 'data/product_details.csv'.")
except Exception as e:
    print(f"Error saving product details: {e}")

driver.quit()
