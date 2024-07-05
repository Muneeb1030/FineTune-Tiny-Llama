import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Or any other WebDriver you are using
driver.get("https://scholar.google.com/citations?user=unGWVYMAAAAJ&hl=en")

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@class='gsc_a_t']/a")))

# Define a function to extract PDF links from a given page
def extract_pdf_links(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    all_links = soup.find_all('a')
    pdf_links = [pdf_link['href'] for pdf_link in all_links if pdf_link.get('href') and ('.pdf' in pdf_link['href'] or 'pdf' in pdf_link['href'].lower())]
    return pdf_links

# Scroll to the end of page to load all results
show_more_button = driver.find_element(By.XPATH, "//*[@id='gsc_bpf_more']//*[@class='gs_lbl']")
show_more_button.click()
time.sleep(2)

# Find all search result links
search_result_links = driver.find_elements(By.XPATH, "//*[@class='gsc_a_t']/a")

# List to store all PDF links
all_pdf_links = []

# Loop through each link
for link in search_result_links:
    # Get the href attribute of the link
    href = link.get_attribute("href")
    # Store the link URL before clicking
    link_url = href
    # Open the link in a new tab using JavaScript to avoid navigation
    driver.execute_script("window.open('" + link_url + "');")
    # Switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*")))
    # Get the page source
    page_source = driver.page_source
    # Extract PDF links from the page source
    pdf_links = extract_pdf_links(page_source)
    # Print PDF links
    if pdf_links:
        print("PDF links on", href, ":", pdf_links)
        all_pdf_links.extend(pdf_links)
        
        # Remove dulicate links
        all_pdf_links = list(set(all_pdf_links))
        
    else:
        print("No PDF links found on", href)
    # Close the current tab
    driver.close()
    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])

# Print all collected PDF links
print("All PDF links:", all_pdf_links)

# Close the browser
driver.quit()

# write links to file
with open('pdf_links.txt', 'w') as f:
    for pdf_link in all_pdf_links:
        f.write(pdf_link + '\n')

folder_path = "pdf_folder"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download PDF files
for pdf_link in all_pdf_links:
    if pdf_link.startswith('http'):
        pdf_url = pdf_link
    else:
        pdf_url = urljoin(href, pdf_link)
    # Download PDF file
    file_name = os.path.join(folder_path, pdf_url.split("/")[-1])
    with open(file_name, 'wb') as f:
        response = requests.get(pdf_url)
        f.write(response.content)
    print("Downloaded:", file_name)