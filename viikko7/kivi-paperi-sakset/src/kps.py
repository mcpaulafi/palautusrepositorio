from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        pass

    def pelaa(self):
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron \
            eli jonkun muun kuin k, p tai s"
        )
        tuomari = Tuomari()

        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            if not self._onko_ok_siirto(ekan_siirto):
                break
            tokan_siirto = self._toisen_siirto()
            if self._onko_ok_siirto(tokan_siirto):
                tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(tuomari)
            else:
                break

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
