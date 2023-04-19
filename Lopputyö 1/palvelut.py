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

    def get_nimi(self):
        return self.__nimi
    
    def get_ika(self):
        return self.__ika
    
    def get_asiakasnro(self):
        return self.__asiakasnro
    
    def set_nimi(self, nimi):
        if nimi == False:
            raise ValueError("Uusi nimi on annettava.")
        if nimi == True:
            self.__nimi = nimi
    
    def set_ika(self, ika):
        if ika == False:
            raise ValueError("Uusi ikä on annettava.")
        if ika == True:
            self.__ika = ika   


class Palvelu(Asiakas):
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(self):
        merkkijono = f'{Asiakas.get_nimi()} {Asiakas.get_asiakasnro()} on {Asiakas.get_ika()}-vuotias'
        self.__asiakkaat.append(merkkijono)

    def lisaa_asiakas(self, Asiakas):
        self.__asiakkaat.append (Asiakas)
        
    def poistaa_asiakas(self, Asiakas):
        self.__asiakkaat.remove (Asiakas)

    def tulosta_asiakkaat(self):
        print(self.__asiakkaat)
        


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
