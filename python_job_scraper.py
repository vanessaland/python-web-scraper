# This web scraper finds all the jobs which are not remote roles

import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="job_list")
job_elements = results.find_all("div", class_="job")

for job_element in job_elements:
    title_element = job_element.find("h1")
    company_element = job_element.find_all("span", class_="info")[3]
    location_element = job_element.find_all("span", class_="info")[0]
    link_url = job_element.find("a")["href"]
    
    if "remote" not in title_element.text.strip().lower() and "remote" not in location_element.text.strip().lower():
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print(f"Apply here: https://pythonjobs.github.io{link_url}\n")
        print()