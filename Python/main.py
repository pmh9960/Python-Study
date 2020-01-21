import requests
import indeed
from save import save_to_file

max_indeed_page = indeed.extract_indeed_pages()
indeed_jobs = indeed.extract_indeed_jobs(max_indeed_page)

save_to_file(indeed_jobs)