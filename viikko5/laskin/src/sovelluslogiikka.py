class BinaariOperaatio:
    def __init__(self, io):
        self.io = io
        self.luku1 = 0
        self.luku2 = 0

    def suorita(self):
        self.luku1 = int(self.io.lue("Luku 1:"))
        self.luku2 = int(self.io.lue("Luku 2:"))

        self.io.kirjoita(f"Vastaus: {self.laske()}")

    def laske(self):
        return 0


class Summa(BinaariOperaatio):
    def __init__(self, io):
        super().__init__(io)

    def laske(self):
        return self.luku1 + self.luku2


class Nollaus(BinaariOperaatio):
    def __init__(self, io):
        super().__init__(io)

    def laske(self):
        self.luku1 = 0
        self.luku2 = 0


class Erotus(BinaariOperaatio):
    def __init__(self, io):
        super().__init__(io)

    def laske(self):
        return self.luku1 - self.luku2


class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
