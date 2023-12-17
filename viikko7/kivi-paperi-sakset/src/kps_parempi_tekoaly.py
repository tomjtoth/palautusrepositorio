from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self, tuomari, tekoaly: TekoalyParannettu):
        super().__init__(tuomari)
        self.tekoaly = tekoaly

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto
