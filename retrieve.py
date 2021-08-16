import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
#for job_element in job_elements:
    #print(job_element, end="\n"*2)
#for job_element in job_elements:
    #title_element = job_element.find("h2", class_="title")
    #company_element = job_element.find("h3", class_="company")
    #location_element = job_element.find("p", class_="location")
    #.text for print to take out the html tags - looks nice now and then use .strip() to take out whitespace
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
    # print()
    #finding python jobs only
    #now all of this h2 string text being converted to lower case and now we look for python
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
#print(len(python_jobs))
#print(python_job_elements)
for python_job in python_job_elements:
    title_element = python_job.find("h2", class_="title")
    company_element = python_job.find("h3", class_="company")
    location_element = python_job.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    #only show the application url, real python had another method which also works
    links = python_job.find_all("a", string=lambda text: "apply" in text.lower())
    #print(links)
    for link in links:
        #appl_link = link.find_all()
        link_url = link['href']
        #print(link)
        #apply = 
        #link_url = link['href']
        #print(type(link_url))
        print(f"Apply here: {link_url}\n")

    
#print(results.prettify())

#print(soup)

