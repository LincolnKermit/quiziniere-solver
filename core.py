from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = input('URL : ')
print("Example : URL : https://www.quiziniere.com/diffusions/OO06S2")

# Set up ChromeOptions to run headless (without opening a browser window)
chrome_options = Options()
chrome_options.add_argument('--headless')

# Create a new Chrome browser session
with webdriver.Chrome(options=chrome_options) as driver:
    # Load the URL
    driver.get(url)

    # Wait for the questions to be loaded (adjust the wait time as needed)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ql-editor')))

    # Get the updated page source after JavaScript execution
    updated_html_source = driver.page_source

# Parse the updated HTML source code
soup = BeautifulSoup(updated_html_source, 'html.parser')

# Find the elements containing the questions (adjust the tag and class accordingly)
text_elements = soup.find_all('div', class_='ql-editor')


# Extract and print the questions


print(f"Intro: a de finir ")
y = 0
for index, question_element in enumerate(text_elements, start=1):
    if y == 3:
        question_text = question_element.get_text(strip=True)
        print(f"Question {index}: {question_element.get_text(strip=True)}")
        y = 0
    else:
        y = y+1
        question_text = question_element.get_text(strip=True)
        print(f"Réponse {index}: {question_text}")
