from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import logging
import csv

# Setup WebDriver
service = Service('./chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=chrome_options)

logging.basicConfig(filename='leetcode_scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List to hold the scraped data
questions_and_answers = []

# Function to scrape a single problem page
def scrape_problem_page(url):
    try:
        driver.get(url)
        time.sleep(10)  # Give the page time to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract the question title
        title_element = soup.find('div', class_='text-title-large font-semibold text-text-primary dark:text-text-primary')
        if not title_element:
            logging.warning(f"Title not found for URL: {url}")
            return None
        title = title_element.text.strip()

        # Extract the problem statement
        problem_statement_element = soup.find('div', class_='elfjS')
        if not problem_statement_element:
            logging.warning(f"Problem statement not found for {title}")
            return None
        problem_statement = problem_statement_element.get_text(separator='\n').strip()
        
        editorial_tab = driver.find_element(By.ID, "editorial_tab")
        if editorial_tab:
            editorial_tab.click()
            time.sleep(10)  # Wait for the editorial tab to load
        codeiframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.execute_script("arguments[0].scrollIntoView(true);", codeiframe)
        driver.switch_to.frame(codeiframe)
        
        time.sleep(10)  # Wait for the editorial tab to load

        lang_buttons = driver.find_elements(By.CLASS_NAME, "lang-btn-set")
        # Extract solutions for different programming languages
        languages = ['Java', 'C++', 'Python3']
        solutions = {}
        
        for language in languages:
            try:
                # Find and click the language toggle button within the same div structure
                for button in lang_buttons:
                    if button.text == language:
                        button.click()
                        time.sleep(2)  # Allow time for the solution to load
                        break
                
                # Reparse the page after changing the language
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                code_editor = soup.select_one('CodeMirror-lines')

                solution = code_editor.get_text(separator='\n').strip() if code_editor else f"No solution found for {language}"
                solutions[language] = solution
                
            except Exception as e:
                logging.warning(f"Could not find solution for {language}: {e}")
                solutions[language] = f"Error retrieving solution for {language}"

        # Extract the date of writing (if available)
        date_element = soup.find('time')
        date_of_writing = date_element.get('datetime') if date_element else "Date not available"

        return {
            'title': title,
            'problem_statement': problem_statement,
            'solutions': solutions,
            'date_of_writing': date_of_writing
        }
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return None

# Function to get problem URLs from the problem set page
def get_problem_urls(limit=8):
    problem_urls = []
    try:
        driver.get('https://leetcode.com/problemset/all/')
        time.sleep(3)

        while len(problem_urls) < limit:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            problem_links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/problems/"]')
           
            for link in problem_links:
                url = link.get_attribute('href')
                if url not in problem_urls:
                    problem_urls.append(url)
                    if len(problem_urls) >= limit:
                        break

            if len(problem_urls) < limit:
                logging.info("No more pages to load or error occurred during pagination.")
                break

        return problem_urls
    except Exception as e:
        logging.error(f"Error retrieving problem URLs: {e}")
        return []

# Scrape each problem page and save to CSV
problem_urls = get_problem_urls(8)  # Limit to 4 questions
for url in problem_urls:
    result = scrape_problem_page(url)
    if result:
        questions_and_answers.append(result)
       

driver.quit()

# Write results to CSV
with open('leetcode_problems_test.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'problem_statement', 'solutions', 'date_of_writing']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for qa in questions_and_answers:
        writer.writerow(qa)

print("Data saved to leetcode_problems_test.csv")
