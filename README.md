# 🛋️ Ecommerce Web Scraper using Selenium
<img src="https://github.com/user-attachments/assets/325f6104-a93c-4735-920d-2df42951f556" alt="Custom Icon" width="1050" height="250">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green?logo=selenium)
![License](https://img.shields.io/badge/License-MIT-red)

A Selenium-based web scraper that extracts product details (title, price, image URL, and description) from Pottery Barn's furniture section. Ideal for price tracking, inventory analysis, or building product catalogs.

---

## 🌟 Features

- 🍪 **Cookie Authentication**: Uses browser cookies for seamless session management
- 📦 **Multi-Format Export**: Saves data to `JSON` (product URLs) and `CSV` (product details)
- 🛋️ **Furniture Focus**: Targets Pottery Barn's sofa category (easily customizable)
- 🛡️ **Error Handling**: Gracefully skips missing elements and logs errors
- 📂 **Structured Output**: Auto-generates organized `data/` folder for results

---

## 📦 Prerequisites

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **Google Chrome**: [Download Chrome](https://www.google.com/chrome/)
3. **Cookies Editor Extension**: [Chrome](https://chrome.google.com/webstore/detail/cookies-editor/) | [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookies-editor/)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/saifee3/ecommerce-web-scraper-using-selenuim.git
cd pottery-barn-scraper
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Cookies (One-Time Setup)
Follow the Cookie Setup Guide below to generate your `cookies.txt` file.

### 4. Run the Scraper
```bash
python script/scraper.py
```

---

## 🍪 Cookie Setup Guide

### Step 1: Install Cookies Editor Extension
1. Open Chrome/Firefox
2. Install **[Cookies Editor](https://chrome.google.com/webstore/detail/cookies-editor/)** from your browser's extension store

### Step 2: Export Active Cookies
1. Navigate to your desired website
2. Log in (if required) and browse to the sofa section
3. Click the **Cookies Editor** extension icon
4. Click **Export** → **Copy to Clipboard**

### Step 3: Save Cookies File
1. Create a `config/` folder in your project
2. Create `cookies.txt` in the `config/` folder
3. Paste the copied cookies (JSON format) and save

---

## Data Extraction Process 📝

### Inspecting the Website Structure
To effectively extract data from AliExpress or any website, it's crucial to understand the underlying HTML structure. Here's how to approach it:

1. **Open Developer Tools**: Right-click on the webpage and select "Inspect" or press `F12` to open Chrome Developer Tools.
2. **Locate Target Elements**: Find the elements containing the data you want to extract (product titles, prices, etc.).
3. **Identify Unique Selectors**: Look for unique class names, IDs, or other attributes that can be used to reliably select these elements.
4. **Consider Hierarchy**: Note the nesting of elements to create more precise selectors that reduce the chance of selecting unintended elements.

### Choosing Between XPaths and CSS Selectors
Both XPaths and CSS selectors have their strengths:
- **CSS Selectors**: Generally faster and more readable, especially for simpler selections. Ideal when targeting elements based on class names, IDs, or direct parent-child relationships.
- **XPaths**: More powerful for complex queries, especially when needing to navigate the DOM tree in more flexible ways or when text content needs to be matched.

### Best Practices for Robust Data Extraction
- **Avoid Fragile Selectors**: Don't rely on classes or IDs that might change frequently or are used inconsistently across the site.
- **Use Relative Paths**: When using XPaths, prefer relative paths over absolute paths to make your selectors more resilient to structure changes.
- **Test Selectors Thoroughly**: Validate your selectors against multiple pages and different search results to ensure consistency.
- **Handle Dynamic Content**: Be aware of elements that might load asynchronously and implement appropriate waiting mechanisms.
- **Document Your Selectors**: Keep a record of the selectors you're using and their purpose, which will be invaluable when maintaining or updating the scraper.

---

## 📂 Folder Structure

```
scraper/
├── script.py                # Main scraping script
├── cookies.txt              # Browser cookies (never commit this!)
├── product_urls.json        # All product page URLs
├── product_details.csv      # Full product dataset
├── requirements.txt         # Python dependencies
└── README.md                # You are here!
```

## ⚙️ Customization

### Change Target Category
Modify the `product_listing_url` in `scraper.py`:
```python
# Current URL 
product_listing_url = "current url"

# Example: Switch to your desired
product_listing_url = "your desired url"
```

### Adjust Wait Times
Modify the sleep durations for slower connections:
```python
time.sleep(20)  # Initial page load → Increase to 30 if needed
time.sleep(3)   # Product page load → Reduce to 2 for faster scraping
```

## 📜 Ethical Scraping

This project follows best practices:
- ⏳ 20-second delay between page loads
- 📉 Limited to 1 concurrent request
- 🔒 Never stores personal/sensitive data

---

## 📄 License
MIT License - Use freely but attribute if redistributed.  

## 🙏 Credits

- **[Selenium](https://www.selenium.dev/)** - The primary automation framework used in this project.  
- **[Python](https://www.python.org/)** - The programming language powering this scraper.  
- **[Real Python](https://realpython.com/modern-web-automation-with-python-and-selenium/)** - Banner image sourced from their tutorial.  
- **[Pottery Barn](https://www.potterybarn.com/)** - The e-commerce website used for data extraction.  
- Banner Image by **Real Python** on https://realpython.com/modern-web-automation-with-python-and-selenium/
