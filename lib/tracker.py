from prca_scrape import callScrape
import csv
import pandas as pd
from datetime import datetime, timedelta


today = str(datetime.today().date())
main_file = 'output.csv'


def scrapeArrayToJson(data):
    data = data
    json = {'campaign_list': {'source': '38 Degrees', 'list': []}}

    for page in data:
        for campaign in page:
            json['campaign_list']['list'].append({
                'title': campaign[0],
                'link': campaign[1],
                'signatures': campaign[2],
                'goal': campaign[3]
            })
    return json


def initialWriteToCSV(data, file):
    rows = data
    with open(file, mode='w') as csv_file:
        fieldnames = ['Campaign Title', 'Link', 'Signatures',
                      'Goal', 'Day Growth', 'Last Written']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            writer.writerow({'Campaign Title': row['title'],
                             'Link': row['link'],
                             'Signatures': row['signatures'],
                             'Goal': row['goal'],
                             'Day Growth': '',
                             'Last Written': today})
    print("Finished writing to CSV.")


def runThirtyEightScript(url, file):
    start = datetime.now()
    start_str = str(start)
    print("Started at: " + start_str)
    print("Working...\n")
    
    # 1. Get data from CallScrape
    new_data = callScrape(url)

    # 2. Convert scraped data to JSON
    output = scrapeArrayToJson(new_data)

    # 3. Check if there is existing CSV data.
    print("Writing to CSV for first time\n...")
    initialWriteToCSV(output, file)
    print("CSV written to for first time.")
    
    end = datetime.now()
    total_time = end - start
    print(total_time)

