import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import re


def getEmployees(company):
    numberStaff = company.find(class_="numberstaff").text
    number = re.sub('\D', '', f'{numberStaff}')
    return int(number)


def getClients(company):
    numberClients = company.find(class_="numberclients").text
    number = re.sub('\D', '', f'{numberClients}')
    return int(number)


def practitionerPage(company):
    website = "https://register.prca.org.uk"
    url = company.find('form').get('action')
    url_fix = url.replace(" ", "%20")
    output = website + url_fix
    print(output)

def calculateSize(size):
    output = ""
    
    if size >= 30:
        output = "Large"
    elif size > 60:
        output = "Very large"
    elif size < 30 and size >= 10:
        output = "Small"
    elif size < 10:
        output = "Very small"
    else:
        output = "CHECK"
    
    return output


def callScrape(url):
    print("Printing: " + url)
    macro_data = []
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    companies = soup.find_all(class_="member-list-profile")

    for company in companies:
        name = company.find('h1').text
        employees = getEmployees(company) 
        clients = getClients(company)
        size = calculateSize(clients)

        data = [name, employees, clients, size]
        macro_data.append(data)


    return macro_data
