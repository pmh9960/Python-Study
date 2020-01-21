import csv

def save_to_file(jobs):
    file = open("indeed_jobs.csv", mode = "w", encoding = "utf-8")
    writer = csv.writer(file)
    writer.writerow(["TITLE", "COMPANY", "LOCATION", "LINK"])
    for job in jobs:
        writer.writerow(list(job.values()))

    return 