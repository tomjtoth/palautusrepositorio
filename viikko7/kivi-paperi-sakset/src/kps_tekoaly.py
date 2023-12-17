from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):

    def __init__(self, tuomari, tekoaly: Tekoaly):
        super().__init__(tuomari)
        self.tekoaly = tekoaly

    def _toisen_siirto(self, _ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
