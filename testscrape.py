import requests
from bs4 import BeautifulSoup
import csv

def scrape_data():
    url = "http://www.oc.edu/events"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    events = soup.find_all('div', class_='event')

    with open('events.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Event Name", "Event Date", "Event Time", "Event Location"])

        for event in events:
            event_name = event.find('h3', class_='event-title').text
            event_date = event.find('time', class_='event-date').text
            event_time = event.find('time', class_='event-time').text
            event_location = event.find('div', class_='event-location').text

            writer.writerow([event_name, event_date, event_time, event_location])

scrape_data()
event_description = event.find('p', class_='event-description').text

writer.writerow([event_name, event_date, event_time, event_location, event_description])

scrape_data()