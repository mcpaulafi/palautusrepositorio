from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

# tehdasfunktio
def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()

    return None

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        peli = luo_peli(vastaus)
        if peli is None:
            print("Loppu.")
            break
        peli.pelaa()

if __name__ == "__main__":
    main()
