from textwrap import dedent
from kps import KPS
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from tuomari import Tuomari

tekoaly = Tekoaly()
parempi_tekoaly = TekoalyParannettu()


def main():
    conf = {
        'a': (
            KPS,
            None,
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s",
        ),
        'b': (
            KPSTekoaly,
            tekoaly,
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        ),
        'c': (
            KPSParempiTekoaly,
            parempi_tekoaly,
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
    }

    while True:
        # resetting tuomari for each game
        tuomari = Tuomari()
        try:
            answer = input(dedent(
                """\
                Valitse pelataanko
                 (a) Ihmistä vastaan
                 (b) Tekoälyä vastaan
                 (c) Parannettua tekoälyä vastaan
                Muilla valinnoilla lopetetaan
                """
            )).lower()

            the_class, the_opponent, the_text = conf[answer[0]]

            print(the_text)

            the_class(tuomari, the_opponent).pelaa()

        except (
            # other than a,b,c
            KeyError,

            # 0 long string
            IndexError
        ):
            break


if __name__ == "__main__":
    main()
