class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto = (self._siirto+1) % 3
        return "kps"[self._siirto]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
