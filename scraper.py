import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch webpage
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to retrieve data. Status code:", response.status_code)
    exit()

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract job details
job_elements = soup.find_all("div", class_="card-content")

jobs = []
for job in job_elements:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    link = job.find("a")["href"]
    
    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Apply_Link": link
    })

# Step 4: Save to CSV
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False, encoding="utf-8")

print(f"✅ Scraped {len(jobs)} jobs and saved to jobs.csv")
