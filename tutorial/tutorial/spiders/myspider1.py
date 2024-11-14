import json


def send_data_to_telegram():
    with open('myspidername.json', 'r') as file:
        data = json.load(file)

        n = 0
        x = len(links)
        # print(x)
        while n < x:    w = f"Title: {titles[n]}\nDate: {ddate[n]}\nLink: {links[n]}\n Location: Usus am Wasser"
        requests.post(
            'https://api.telegram.org/bot7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE' % w)
        n += 1

        event_title = data[n]['event_link']
        event_date = data[n]['date']
        event_location = data[n]['location']

        print(f"Title: {event_title}")
        print(f"Date: {event_date}")
        print(f"Location: {event_location}")


send_data_to_telegram()