import random

class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__asiakasnro = self.__luo_nro()
        self.__ika = ika

    def __luo_nro():
        numerot = []
        for i in range(3):
            x = random.randint(10, 99)
            y = random.randint(100, 999)
            z = random.randint(100, 999)
            numerot.append (f"{x}-{y}-{z}")


class Palvelu(Asiakas):
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(self, Asiakas):
        pass

    def lisaa_asiakas(self, Asiakas):
        self.__asiakkaat.append (Asiakas)
        
    def poistaa_asiakas(self, Asiakas):
        self.__asiakkaat.remove (Asiakas)

    def tulosta_asiakkaat():
        pass
        


class ParempiPalvelu(Palvelu):
    def __init__(self, nimi, kuvaus, hinta, ominaisuudet):
        super().__init__(nimi, kuvaus, hinta)
        self.__edut = ominaisuudet

    def listaa_etu():
        pass

    def poistaa_etu():
        pass

    def tulosta_edut():
        pass
