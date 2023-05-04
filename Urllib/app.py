from oliot import WebData

google_data = WebData('https://www.google.com')
parsed_data = google_data.PalautaJasennetty()

for item in parsed_data:
    if '<head' in item:
        print(item + '>')
        break
