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
        self.nimi2 = "simo"
        self.tilinro2 = "22223"

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
            if tuote_id == 3:
                return 100

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 10)
            if tuote_id == 3:
                return Tuote(3, "voi", 100)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tilinro)

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla_kun_1_tuote(self):

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tilinro)

        tuote_hinta = self.varasto_mock.hae_tuote(1).hinta

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, 42, self.tilinro, "33333-44455", tuote_hinta)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla_kun_2_tuotetta(self):

        # palautetaan aina arvo 22
        self.viitegeneraattori_mock.uusi.return_value = 22

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu(self.nimi, self.tilinro)

        tuote_hinta1 = self.varasto_mock.hae_tuote(1).hinta
        tuote_hinta3 = self.varasto_mock.hae_tuote(3).hinta
        kori_summa = tuote_hinta1 + tuote_hinta3

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, self.viitegeneraattori_mock.uusi(), self.tilinro, "33333-44455", kori_summa)


    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla_kun_toinen_loppu(self):

        # palautetaan aina arvo 22
        self.viitegeneraattori_mock.uusi.return_value = 22

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2) #Ei lisätä koska tuotetta saldolla 0
        self.kauppa.tilimaksu(self.nimi, self.tilinro)

        tuote_hinta1 = self.varasto_mock.hae_tuote(1).hinta
        kori_summa = tuote_hinta1

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(self.nimi, self.viitegeneraattori_mock.uusi(), self.tilinro, "33333-44455", kori_summa)

    def test_ostoksen_paatyttya_uusi_ostos_saa_hinnan_nolla(self):

        # palautetaan 1 ja sen jälkeen 2
        self.viitegeneraattori_mock.uusi.side_effect = [1,2]

        # tehdään ekat ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tilinro)

        # aloitetaan toinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.nimi2, self.tilinro2)

        # ostoskorin summa
        kori_summa = self.varasto_mock.hae_tuote(3).hinta

        # varmistetaan, että metodia tilisiirto on kutsuttu tuotteen 2 hinnalla
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, kori_summa)


# Varmista, että kauppa pyytää uuden viitenumeron jokaiselle maksutapahtumalle, 
# katso tarvittaessa apua tehtävän 1 projektin mock-demo testeistä!
    def test_kaytetaan_perakkaisten_viitekutsujen_arvoja(self):

        # määritellään että metodi palauttaa ensimmäisellä kutsulla 1, toisella, 2...
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        # tehdään ekat ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(self.nimi, self.tilinro)

        # varmistetaan, että viitenumero on 1
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)

        # aloitetaan ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(self.nimi2, self.tilinro2)

        # varmistetaan, että viitenumero on 2
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)


#Tuotteen poistaminen
    def test_tuote_poistetaan_korista_metodia_palauta_varastoon_kutsutaan(self):

        #self.viitegeneraattori_mock.uusi.side_effect = 12

        # aloitetaan ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.poista_korista(1)
        #self.kauppa.tilimaksu(self.nimi2, self.tilinro2)

        #tuote3 = self.varasto_mock.hae_tuote(3)
        self.varasto_mock.palauta_varastoon.assert_called()


    def test_tuote_poistetaan_korista_metodia_palauta_varastoon_kutsutaan(self):

        self.viitegeneraattori_mock.uusi.side_effect = [12,13]

        # aloitetaan ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu(self.nimi2, self.tilinro2)

        tuote1 = self.varasto_mock.hae_tuote(1)
        self.varasto_mock.palauta_varastoon.assert_called_with(tuote1)

