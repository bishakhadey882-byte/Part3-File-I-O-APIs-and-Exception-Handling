# ============================================================
# Task 1 — File Read & Write Basics
# ============================================================

# -------------------------
# PART A — Write
# -------------------------

# Writing 5 student notes to python_notes.txt using write mode ('w')
# 'w' mode creates the file if it doesn't exist, or overwrites it if it already does
# encoding="utf-8" ensures proper handling of all characters

with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully.")

# Appending two more lines using append mode ('a')
# 'a' mode adds to the file without deleting existing content

with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code and improve readability.\n")
    file.write("Topic 7: Modules allow us to organize and import code easily.\n")

print("Lines appended.")

# -------------------------
# PART B — Read
# -------------------------

# 1. Read the file and print each line numbered (strip removes trailing \n)
print("\n--- Numbered Lines ---")
with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

# 2. Count and print total number of lines
print(f"\nTotal number of lines in the file: {len(lines)}")

# 3. Ask user for a keyword and print all matching lines (case-insensitive)
keyword = input("\nEnter a keyword to search: ")
matches = [line.strip() for line in lines if keyword.lower() in line.lower()]

if matches:
    print(f"\nLines containing '{keyword}':")
    for match in matches:
        print(match)
else:
    print(f"No lines found containing the keyword '{keyword}'.")






# ============================================================
# Task 2 — API Integration
# Using DummyJSON Products API: https://dummyjson.com/products
# ============================================================

import requests

BASE_URL = "https://dummyjson.com/products"

# ============================================================
# STEP 1 — Fetch and Display 20 Products
# ============================================================

print("=" * 72)
print("STEP 1: Fetching 20 products")
print("=" * 72)

response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
data = response.json()
products = data["products"]

# Print formatted table exactly as required
print(f"{'ID':<5}| {'Title':<33}| {'Category':<18}| {'Price':<10}| {'Rating'}")
print("-" * 5 + "|" + "-" * 34 + "|" + "-" * 19 + "|" + "-" * 11 + "|" + "-" * 8)

for p in products:
    print(f"{p['id']:<5}| {p['title']:<33}| {p['category']:<18}| ${p['price']:<9}| {p['rating']}")

# ============================================================
# STEP 2 — Filter (rating >= 4.5) and Sort by Price Descending
# ============================================================

print("\n" + "=" * 72)
print("STEP 2: Filtered (rating >= 4.5) and Sorted by Price (Descending)")
print("=" * 72)

filtered = [p for p in products if p["rating"] >= 4.5]
sorted_products = sorted(filtered, key=lambda p: p["price"], reverse=True)

print(f"{'ID':<5}| {'Title':<33}| {'Category':<18}| {'Price':<10}| {'Rating'}")
print("-" * 5 + "|" + "-" * 34 + "|" + "-" * 19 + "|" + "-" * 11 + "|" + "-" * 8)

for p in sorted_products:
    print(f"{p['id']:<5}| {p['title']:<33}| {p['category']:<18}| ${p['price']:<9}| {p['rating']}")

# ============================================================
# STEP 3 — Search by Category: Laptops
# ============================================================

print("\n" + "=" * 72)
print("STEP 3: All products in 'laptops' category")
print("=" * 72)

laptop_response = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
laptops = laptop_response.json()["products"]

for laptop in laptops:
    print(f"Name: {laptop['title']}  |  Price: ${laptop['price']}")

# ============================================================
# STEP 4 — POST Request (Simulated)
# ============================================================

print("\n" + "=" * 72)
print("STEP 4: Sending POST request to add a new product (simulated)")
print("=" * 72)

# Note: DummyJSON simulates a create — no data is actually stored on the server
new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

post_response = requests.post(f"{BASE_URL}/add", json=new_product, timeout=5)
print("Full response from server:")
print(post_response.json())






# ============================================================
# Task 3 — Exception Handling
# This file covers Parts A, B, C, and D
# It also updates all API calls from Task 2 with try-except blocks
# ============================================================

import requests


BASE_URL = "https://dummyjson.com/products"

# ============================================================
# PART A — Guarded Calculator: safe_divide(a, b)
# ============================================================

def safe_divide(a, b):
    """
    Divides a by b.
    - Returns the result of a / b on success
    - Catches ZeroDivisionError if b is 0
    - Catches TypeError if a or b is not a number
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print("=" * 50)
print("PART A: safe_divide Tests")
print("=" * 50)
print(safe_divide(10, 2))       # Expected: 5.0
print(safe_divide(10, 0))       # Expected: Error: Cannot divide by zero
print(safe_divide("ten", 2))    # Expected: Error: Invalid input types

# ============================================================
# PART B — Guarded File Reader: read_file_safe(filename)
# ============================================================

def read_file_safe(filename):
    """
    Tries to open and read the given file.
    - Returns full content as a string if successful
    - Catches FileNotFoundError and prints a clear message
    - Uses finally block to always print 'File operation attempt complete.'
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    finally:
        # This ALWAYS runs — whether file was found or not
        print("File operation attempt complete.")

print("\n" + "=" * 50)
print("PART B: read_file_safe Tests")
print("=" * 50)

print("\nTest 1: python_notes.txt (should succeed)")
result = read_file_safe("python_notes.txt")
if result:
    print(result)

print("\nTest 2: ghost_file.txt (should fail gracefully)")
read_file_safe("ghost_file.txt")

# ============================================================
# PART C — Robust API Calls (Task 2 code updated with try-except)
# Every requests.get() and requests.post() is wrapped in try-except
# ============================================================

def fetch_products():
    """Fetch 20 products — wrapped in try-except for robustness."""
    print("\n" + "=" * 50)
    print("PART C: Fetching 20 products (robust)")
    print("=" * 50)
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        data = response.json()
        products = data["products"]
        print(f"{'ID':<5}| {'Title':<33}| {'Category':<18}| {'Price':<10}| {'Rating'}")
        print("-" * 75)
        for p in products:
            print(f"{p['id']:<5}| {p['title']:<33}| {p['category']:<18}| ${p['price']:<9}| {p['rating']}")
        return products
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
        return []
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def filter_and_sort(products):
    """Filter products with rating >= 4.5 and sort by price descending."""
    filtered = [p for p in products if p["rating"] >= 4.5]
    return sorted(filtered, key=lambda p: p["price"], reverse=True)


def fetch_laptops():
    """Fetch laptops category — wrapped in try-except."""
    print("\n" + "=" * 50)
    print("PART C: Fetching laptops category (robust)")
    print("=" * 50)
    try:
        response = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
        laptops = response.json()["products"]
        for laptop in laptops:
            print(f"Name: {laptop['title']}  |  Price: ${laptop['price']}")
        return laptops
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
        return []
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def post_product():
    """Send POST request — wrapped in try-except."""
    print("\n" + "=" * 50)
    print("PART C: POST new product (robust)")
    print("=" * 50)
    try:
        new_product = {
            "title": "My Custom Product",
            "price": 999,
            "category": "electronics",
            "description": "A product I created via API"
        }
        response = requests.post(f"{BASE_URL}/add", json=new_product, timeout=5)
        print("Server Response:", response.json())
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Run Part C functions
products = fetch_products()

if products:
    sorted_products = filter_and_sort(products)
    print("\n--- Filtered & Sorted (rating >= 4.5, price descending) ---")
    for p in sorted_products:
        print(f"{p['id']:<5}| {p['title']:<33}| ${p['price']:<9}| {p['rating']}")

fetch_laptops()
post_product()

# ============================================================
# PART D — Input Validation Loop
# ============================================================

print("\n" + "=" * 50)
print("PART D: Product ID Lookup Loop")
print("=" * 50)

while True:
    user_input = input("\nEnter a product ID to look up (1-100), or 'quit' to exit: ")

    # Check if user wants to quit
    if user_input.strip().lower() == "quit":
        print("Exiting product lookup. Goodbye!")
        break

    # Validate: must be an integer in range 1–100
    try:
        product_id = int(user_input)
        if product_id < 1 or product_id > 100:
            print("Warning: Please enter a number between 1 and 100.")
            continue   # Do NOT make API call — go back and ask again
    except ValueError:
        print("Warning: Invalid input. Please enter a whole number.")
        continue       # Do NOT make API call — go back and ask again

    # Only reaches here if input is valid
    try:
        response = requests.get(f"{BASE_URL}/{product_id}", timeout=5)

        if response.status_code == 404:
            # 404 means product was not found — not a Python exception
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"Title: {product['title']}")
            print(f"Price: ${product['price']}")
        else:
            print(f"Unexpected response code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"Unexpected error: {e}")






# ============================================================
# Task 4 — Logging to File
# Builds an error logger that writes timestamped entries
# to error_log.txt whenever an exception or bad response occurs
# ============================================================

import requests
from datetime import datetime

LOG_FILE = "error_log.txt"
BASE_URL = "https://dummyjson.com/products"


def log_error(function_name, error_type, message):
    """
    Writes a timestamped error entry to error_log.txt.

    Format:
    [YYYY-MM-DD HH:MM:SS] ERROR in function_name: ErrorType - message

    Opens file in append mode ('a') so entries accumulate across runs.
    Uses datetime.now() as required by the assignment.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n"

    # Append mode so previous logs are never overwritten
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

    print(f"Logged → {log_entry.strip()}")


# ============================================================
# Logged Entry 1 — Trigger a ConnectionError
# Using a genuinely unreachable URL as required by the assignment
# ============================================================

print("=" * 65)
print("Triggering ConnectionError (unreachable URL)...")
print("=" * 65)

try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError:
    log_error("fetch_products", "ConnectionError", "No connection could be made")
except requests.exceptions.Timeout:
    log_error("fetch_products", "TimeoutError", "Request timed out")
except Exception as e:
    log_error("fetch_products", "UnexpectedError", str(e))

# ============================================================
# Logged Entry 2 — Trigger an HTTP 404 Error
# Product ID 999 does not exist on DummyJSON
# IMPORTANT: 404 is NOT a Python exception — we check status_code manually
# and log it inside an if block, NOT inside except
# ============================================================

print("\n" + "=" * 65)
print("Triggering HTTP 404 Error (product ID 999 does not exist)...")
print("=" * 65)

try:
    response = requests.get(f"{BASE_URL}/999", timeout=5)

    # Check HTTP status manually — 404 is a response, not a Python exception
    if response.status_code != 200:
        log_error(
            "lookup_product",
            "HTTPError",
            f"{response.status_code} Not Found for product ID 999"
        )
    else:
        product = response.json()
        print(f"Product found: {product['title']}")

except requests.exceptions.ConnectionError:
    log_error("lookup_product", "ConnectionError", "No connection could be made")
except requests.exceptions.Timeout:
    log_error("lookup_product", "TimeoutError", "Request timed out")
except Exception as e:
    log_error("lookup_product", "UnexpectedError", str(e))

# ============================================================
# Read and Print Full Contents of error_log.txt
# This proves to the examiner that logging is working correctly
# ============================================================

print("\n" + "=" * 65)
print("Full contents of error_log.txt:")
print("=" * 65)

with open(LOG_FILE, "r", encoding="utf-8") as log_file:
    print(log_file.read())
