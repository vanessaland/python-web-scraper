# This web scraper finds all the job postings which are Python related

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
    
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for python_job in python_job_elements:
    title_element = python_job.find("h2", class_="title")
    company_element = python_job.find("h3", class_="company")
    location_element = python_job.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
    link_url = python_job.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")