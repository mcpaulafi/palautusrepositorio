from kps import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):

    def __init__(self):
        pass

    def _toisen_siirto(self):
        tekoaly = Tekoaly()
        tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokoneen siirto: {tokan_siirto}")
        return tokan_siirto
