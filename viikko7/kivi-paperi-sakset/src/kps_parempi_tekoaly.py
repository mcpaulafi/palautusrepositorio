from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        pass

    def _toisen_siirto(self):
        tekoaly = TekoalyParannettu(10)
        tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokoneen siirto: {tokan_siirto}")
        return tokan_siirto


