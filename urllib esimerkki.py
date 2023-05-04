
# Tuomme urlopen metodin urllib API:sta
from urllib.request import urlopen

response = None

#kokeillaan koodia virhetilanteiden varalta
try:
    response = urlopen("https://www.google.com")
#Näytetää virheilmoitus jos sellainen ilmenee
except Exception as ex:
    print(ex)
else:
    body = response.read()
finally:
    if response is not None:
        response.close()
print(body)
