
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

def extract_indeed_pages():
    
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[0:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page
    
def extract_job(html):
    title = html.find("div", {"class" : "title"}).find("a")["title"]
    
    company = html.find("div", {"class" : "sjcl"}).find("div").find("span", {"class" : "company"})
    company_anchor = company.find("a")
    if company_anchor is not None :
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()

    location = html.find("div", {"class" : "sjcl"}).find("div", {"class" : "recJobLoc"})["data-rc-loc"]
    
    job_id = html["data-jk"]
    link = f"https://kr.indeed.com/viewjob?jk={job_id}"

    return {
        'title' : title, 
        'company' : company, 
        'location' : location, 
        'link' : link}

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(2):   #range(last_page)
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs