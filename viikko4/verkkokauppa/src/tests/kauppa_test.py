import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()
        self.nimi = "pekka"
        self.tilinro = "12345"


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu(self.nimi, self.tilinro)

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla_kun_1_tuote(self):

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu(self.nimi, self.tilinro)

        tuote_hinta = varasto_hae_tuote(1).hinta

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, self.viitegeneraattori_mock.uusi(), self.tilinro, "33333-44455", tuote_hinta)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla_kun_2_tuotetta(self):

        # palautetaan aina arvo 22
        self.viitegeneraattori_mock.uusi.return_value = 22

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 7)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu(self.nimi, self.tilinro)

        tuote_hinta1 = varasto_hae_tuote(1).hinta
        tuote_hinta2 = varasto_hae_tuote(2).hinta
        kori_summa = tuote_hinta1 + tuote_hinta2

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, self.viitegeneraattori_mock.uusi(), self.tilinro, "33333-44455", kori_summa)


# Aloitetaan asiointi, koriin lisätään tuote, jota on varastossa tarpeeksi 
# ja tuote joka on loppu ja suoritetaan ostos, varmista että kutsutaan pankin 
# metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla_kun_toinen_loppu(self):

        # palautetaan aina arvo 22
        self.viitegeneraattori_mock.uusi.return_value = 22

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 20

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 0)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2) #Ei lisätä koska tuotetta saldolla 0
        kauppa.tilimaksu(self.nimi, self.tilinro)

        tuote_hinta1 = varasto_hae_tuote(1).hinta
        #tuote_hinta2 = varasto_hae_tuote(2).hinta
        kori_summa = tuote_hinta1

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, self.viitegeneraattori_mock.uusi(), self.tilinro, "33333-44455", kori_summa)
