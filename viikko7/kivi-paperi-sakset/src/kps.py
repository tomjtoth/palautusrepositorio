from tuomari import Tuomari


class KPS:
    def __init__(self, tuomari: Tuomari, _the_opponent=None):
        self.tuomari = tuomari

    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)
            if not (self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)):
                break
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    # oletuksena PvP jotta pääsisin eroon 1 kokonaisesta luokasta
    def _toisen_siirto(self, _ekan_siirto: str):
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto: str):
        return siirto in ('k', 'p', 's')
