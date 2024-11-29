class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return True
        else:
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.kasvata_lista()
            return True

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kasvata_lista(self):
        self.ljono.extend([0] * self.kasvatuskoko)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for i in a.to_int_list():
            x.lisaa(i)
        for j in b.to_int_list():
            x.lisaa(j)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        for i in a.to_int_list():
            for j in b.to_int_list():
                if i == j:
                    y.lisaa(j)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        for i in a.to_int_list():
            z.lisaa(i)
        for j in b.to_int_list():
            z.poista(j)
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
