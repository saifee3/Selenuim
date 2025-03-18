# 🛋️ Ecommerce Web Scraper using Selenium
![image](https://github.com/user-attachments/assets/325f6104-a93c-4735-920d-2df42951f556)
     Credits: Banner Image by Real Python on https://realpython.com/modern-web-automation-with-python-and-selenium/

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
1. Navigate to **[Pottery Barn](https://www.potterybarn.com/)**
2. Log in (if required) and browse to the sofa section
3. Click the **Cookies Editor** extension icon
4. Click **Export** → **Copy to Clipboard**

### Step 3: Save Cookies File
1. Create a `config/` folder in your project
2. Create `cookies.txt` in the `config/` folder
3. Paste the copied cookies (JSON format) and save

---

## 📂 Folder Structure

```
scraper/
├── script.py                # Main scraping script
├── cookies.txt          # Browser cookies (never commit this!)
├── product_urls.json    # All product page URLs
├── product_details.csv  # Full product dataset
├── requirements.txt         # Python dependencies
└── README.md                # You are here!
```

## ⚙️ Customization

### Change Target Category
Modify the `product_listing_url` in `scraper.py`:
```python
# Current URL (sofas)
product_listing_url = "https://www.potterybarn.com/shop/furniture/sofa/..."

# Example: Switch to dining chairs
product_listing_url = "https://www.potterybarn.com/shop/furniture/dining-chairs/"
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
```

---

This README includes:  
✅ Visual hierarchy with emojis and badges  
✅ Step-by-step cookie setup guide  
✅ Clear troubleshooting section  
✅ Ethical scraping guidelines  
✅ Easy-to-scan code snippets  
✅ Responsive folder structure visualization  

Let me know if you need adjustments! 😊
