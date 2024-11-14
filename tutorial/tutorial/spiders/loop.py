import json
import requests
from datetime import datetime

    json_file = 'loop.json'
    with open(json_file, 'r') as file:
        data = json.load(file)

# Skontrolujeme, či je načítaný súbor zoznam a získame prvý prvok
if isinstance(data, list) and len(data) > 0:
    first_item = data[0]  # Prvý prvok zoznamu

    # Získanie údajov o eventoch
    events = first_item.get('events', [])

    # Tvoj Telegram bot token
    token = '7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE'
    method = "sendMessage"
    chat_id = -1002353949803  # ID Telegram skupiny

    # Inicializácia prázdneho zoznamu pre uloženie neúspešných odoslaní
    failed_events = []

    today_date = datetime.today().strftime('%Y-%m-%d')

    # Spracovanie každého eventu
    for event in events:
        title = event.get('title', 'No Title')  # Ošetríme chýbajúce kľúče
        event_date = event.get('date', 'No Date')
        image_url = event.get('image', 'No Image')

        # Kontrola, či je dátum dnešný
        if event_date == today_date:
            # Kombinovaná správa s názvom, dátumom, a odkazom na obrázok
            message = (f"📌 Event: {title}\n"
                       f"📅 Date: {event_date}\n"
                       f"📍 Location: LOOP\n"
                       f"🔗 Link: https://loop.co.at/events/\n"
                       f"🖼️ Image: {image_url}")

            # Pošleme správu pomocou Telegram API
            response = requests.post(f'https://api.telegram.org/bot7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE/sendMessage', data={
                '2057134887': chat_id,
                'text': message
            })

            # Skontrolujeme, či bola správa úspešne odoslaná
            if response.status_code != 200:
                failed_events.append(title)  # Pridáme názov eventu do zoznamu neúspešných

    # Výpis neúspešných odoslaní (ak nejaké sú)
    if failed_events:
        print("Failed to send messages for the following events:")
        for failed in failed_events:
            print(failed)
    else:
        print("All messages were successfully sent!")

else:
    print("The JSON structure is not as expected or the list is empty.")