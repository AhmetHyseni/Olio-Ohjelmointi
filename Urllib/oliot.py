from urllib.request import urlopen
from chardet import detect

class WebData:
    def __init__(self, WebSivu):
        self.WebSisaltoRaaka = None
        self.WebSisaltojasennetty = None
        
        # get the raw web data using urlopen method
        response = urlopen(WebSivu)
        self.WebSisaltoRaaka = response.read()
        response.close()

        # detect the encoding format and decode the byte string
        encoding = detect(self.WebSisaltoRaaka)['encoding']
        self.WebSisaltoRaaka = self.WebSisaltoRaaka.decode(encoding)

    def PalautaRaaka(self):
        return self.WebSisaltoRaaka

    def PalautaJasennetty(self):
        # split the string by '>'
        self.WebSisaltojasennetty = self.WebSisaltoRaaka.split('>')
        return self.WebSisaltojasennetty
