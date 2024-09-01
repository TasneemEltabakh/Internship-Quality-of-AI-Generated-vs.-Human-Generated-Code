from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import re
import os

# Function to parse HTML code blocks to Python code
def parse_html_to_python(html_code_block):
    lines = html_code_block.split('\n')
    solution_flag = True
    python_flag = True
    if '<span class="hljs-class">' not in lines[0]:
        solution_flag = False
    res = [re.sub('</span>', '', re.sub(r'<span class="hljs-[\s\S]*?">', '', line)) for line in lines] # for code formatting / coloring
    res = [re.sub('&gt;', '>', re.sub('&lt;', '<', line)) for line in res] # HTML entities
    res = '\n'.join(res)
    if '(self,' not in res:
        python_flag = False
    return solution_flag and python_flag, res

def parse_html_to_python_2(html_code_block):
    lines = html_code_block.split('\n')
    solution_flag = True
    python_flag = True
    if 'Solution' not in lines[0]:
        solution_flag = False
    res = [re.sub('</span>', '', re.sub(r'<span[\s\S]*?>', '', line)) for line in lines] # for code formatting / coloring
    res = [re.sub('&gt;', '>', re.sub('&lt;', '<', line)) for line in res] # HTML entities
    res = '\n'.join(res)
    if '(self,' not in res:
        python_flag = False
    return solution_flag and python_flag, res

# Dark mode plotting
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)

pd.set_option('display.max_colwidth', None)

dataset_path = 'dataset'
original_solutions_path = 'problem_solutions'

def get_premium_info(el):
    '''
    Searches a specific div element given as argument for an orange svg object, which indicates the bounding box for the leetcode premium lock symbol on the left of a problem.
    This svg is only present for premium problems.
    '''
    try:
        el.find_element(By.CLASS_NAME, 'text-brand-orange')
    except NoSuchElementException:
        return False
    return True

def scrape_problems_list(num_pages=50, problems_per_page=50):
    '''
    Scrapes master list of problems on leetcode in order to get a dataset of hyperlinks (or equivalently, slugs) to the page dedicated to each individual problem.
    '''
    problems_dict = defaultdict(list)
    for i in range(num_pages):
        print(f"Page: {i+1}")
        source_page = f'https://leetcode.com/problemset/all/?page={i+1}'
        driver = webdriver.Chrome()
        driver.get(source_page)
        time.sleep(60) if (i and not i % 10) else time.sleep(5)
        all_rows = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]')
        j = 0
        while j < problems_per_page:
            try:
                problem_row = all_rows.find_element(By.XPATH, f'./div[{j + 1}]')
                elements = problem_row.find_elements(By.CLASS_NAME, 'mx-2')
                problems_dict['premium'].append(get_premium_info(elements[0]))
                problems_dict['href'].append(elements[1].find_element(By.XPATH, './/div/div/div/div/a').get_attribute('href'))
                problems_dict['title'].append(elements[1].find_element(By.XPATH, './/div/div/div/div/a').text)
                problems_dict['acceptance'].append(elements[3].find_element(By.XPATH, './/span').text)
                problems_dict['difficulty'].append(elements[4].find_element(By.XPATH, './/span').text)
            except NoSuchElementException:
                print(f'Fewer than {problems_per_page} problems on this page.')
            j += 1
    return pd.DataFrame(problems_dict)

def scrape_solutions_forum(problem_slug, num_pages=4):
    '''
    Scrapes the solutions forum dedicated to a given problem (specified via problem slug) to get a dataset of hyperlinks to the top 60 posts (by votes) with the 'python3' tag for that problem.
    '''
    post_dict = defaultdict(list)
    for i in range(1, num_pages + 1):
        source_page = f'https://leetcode.com/problems/{problem_slug}/discuss/?currentPage={i}&orderBy=most_votes&query=&tag=python3'
        driver = webdriver.Chrome()
        driver.get(source_page)
        driver.implicitly_wait(5)
        current_page_posts = driver.find_elements(By.CLASS_NAME, 'topic-item-wrap__2FSZ')
        for post in current_page_posts:
            href = post.find_element(By.XPATH, './/*[@class="topic-item__1Asc"]/div[1]/div[1]/a').get_attribute('href')
            title = post.find_element(By.XPATH, './/*[@class="topic-item__1Asc"]/div[1]/div[1]/a/div/div').text
            try:
                user = post.find_element(By.XPATH, './/*[@class="topic-item__1Asc"]/div[1]/div[2]/span/span[1]/a').text
            except NoSuchElementException:
                user = 'deleted_user'
            upvotes = post.find_element(By.XPATH, './/*[@class="topic-item__1Asc"]/div[2]/div[1]/div').text
            views = post.find_element(By.XPATH, './/*[@class="topic-item__1Asc"]/div[2]/div[2]/div').text
            try:
                post_date = post.find_element(By.XPATH, './/*[@class="topic-item__1Asc"]/div[1]/div[2]/span/span[2]').text
            except NoSuchElementException:
                post_date = 'unknown'
            post_dict['slug'].append(problem_slug)
            post_dict['title'].append(title)
            post_dict['user'].append(user)
            post_dict['upvotes'].append(upvotes)
            post_dict['views'].append(views)
            post_dict['href'].append(href)
            post_dict['date'].append(post_date)
        time.sleep(2)
    return pd.DataFrame(post_dict)

def parse_html_to_python(html_code_block):
    lines = html_code_block.split('\n')
    solution_flag = True
    python_flag = True
    if '<span class="hljs-class">' not in lines[0]:
        solution_flag = False
    res = [re.sub('</span>', '', re.sub('<span class="hljs-[\s\S]*?">', '', line)) for line in lines] # for code formatting / coloring
    res = [re.sub('&gt;', '>', re.sub('&lt;', '<', line)) for line in res] # HTML entities
    res = '\n'.join(res)
    if '(self,' not in res:
        python_flag = False
    return solution_flag and python_flag, res

def parse_html_to_python_2(html_code_block):
    lines = html_code_block.split('\n')
    solution_flag = True
    python_flag = True
    if 'Solution' not in lines[0]:
        solution_flag = False
    res = [re.sub('</span>', '', re.sub('<span[\s\S]*?>', '', line)) for line in lines] # for code formatting / coloring
    res = [re.sub('&gt;', '>', re.sub('&lt;', '<', line)) for line in res] # HTML entities
    res = '\n'.join(res)
    if '(self,' not in res:
        python_flag = False
    return solution_flag and python_flag, res

def scrape_single_post(post_href):
    '''
    Scrapes a single post to return the text written in the original post. Comments are ignored.
    '''
    driver = webdriver.Chrome()
    driver.get(post_href)
    driver.implicitly_wait(5)
    original_post_body = driver.find_elements(By.XPATH, '//*[@id="discuss-container"]/div/div/div[2]/div[1]/div[2]/div[2]/div')#[0]
    try:
        code_blocks = original_post_body.find_elements(By.XPATH, './/pre') # <pre> </pre> used for code formatting
    except NoSuchElementException:
        pass # No code blocks in the original post
    all_solutions_in_post = []
    for block in code_blocks:
        html = block.find_element(By.XPATH, './/code').get_attribute('innerHTML')
        valid_solution, parsed_html = parse_html_to_python(html)
        if valid_solution:
            all_solutions_in_post.append(parsed_html)
    return all_solutions_in_post

def scrape_single_post_2(post_href):
    '''
    Scrapes a single post to return the text written in the original post. Comments are ignored.
    '''
    driver = webdriver.Chrome()
    driver.get(post_href)
    driver.implicitly_wait(5)
    original_post_body = driver.find_elements(By.CLASS_NAME, 'break-words')[0]
    try:
        code_blocks = original_post_body.find_elements(By.XPATH, './/div/div/div/div/pre') # <pre> </pre> used for code formatting
    except NoSuchElementException:
        pass # No code blocks in the original post
    all_solutions_in_post = []
    for block in code_blocks:
        html = block.find_element(By.XPATH, './/code').get_attribute('innerHTML')
        valid_solution, parsed_html = parse_html_to_python_2(html)
        if valid_solution:
            all_solutions_in_post.append(parsed_html)
    return all_solutions_in_post

# Scrape problems list and preprocess for a list of all problem names, slugs, numbers, acceptance rates, and difficulties.
problems_df = scrape_problems_list()  # Uncomment to rescrape data
problems_df.to_csv(f'{dataset_path}/problems_data.csv')

problems_df = pd.read_csv(f'{dataset_path}/problems_data.csv', index_col='Unnamed: 0')
problems_df['number'] = problems_df['title'].str.split('.').map(lambda x: x[0]).astype('int64')
problems_df['title_text'] = problems_df['title'].str.split('.').map(lambda x: x[1]).str[1:]
problems_df['slug'] = problems_df['href'].str.split('/').map(lambda x: x[-2])
problems_df['acceptance'] = problems_df['acceptance'].map(lambda x: float(re.findall(r'\d+\.\d+', x)[0]) if pd.notnull(x) else np.nan)
problems_df['difficulty'] = problems_df['difficulty'].map(lambda x: re.findall(r'[A-Za-z]', x)[0] if pd.notnull(x) else 'unknown')
problems_df.to_csv(f'{dataset_path}/problems_data.csv')

# Extract links from the problems_df dataframe
all_problems_links = problems_df['href'].tolist()
all_problems_slugs = problems_df['slug'].tolist()

# Scrape the solutions forum for each problem and save to CSV
all_posts_dicts = []
for slug in all_problems_slugs:
    try:
        df = scrape_solutions_forum(slug)
        all_posts_dicts.append(df)
    except WebDriverException:
        print(f'Failed to scrape problem {slug}')
    time.sleep(2)  # Avoid rate limits

all_posts_df = pd.concat(all_posts_dicts, ignore_index=True)
all_posts_df.to_csv(f'{dataset_path}/all_posts_hrefs.csv', index=False)

def filter_posts_by_date(df, cutoff_year=2015):
    '''
    Filters posts to only include those posted before a certain year.
    '''
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df[df['date'].dt.year < cutoff_year]
    return df

# Apply filtering after scraping
all_posts_df = pd.read_csv(f'{dataset_path}/all_posts_hrefs.csv', index_col=0)
filtered_posts_df = filter_posts_by_date(all_posts_df)
filtered_posts_df.to_csv(f'{dataset_path}/filtered_posts_hrefs.csv', index=False)

# Optionally scrape individual posts and save their solutions
filtered_posts_df = pd.read_csv(f'{dataset_path}/filtered_posts_hrefs.csv', index_col=0)
all_solutions = []
for href in filtered_posts_df['href']:
    try:
        solutions = scrape_single_post(href)
        all_solutions.extend(solutions)
    except WebDriverException:
        print(f'Failed to scrape post {href}')
    time.sleep(2)  # Avoid rate limits

# Save solutions to a file
with open(f'{dataset_path}/all_solutions.txt', 'w') as file:
    for solution in all_solutions:
        file.write(f"{solution}\n\n")
