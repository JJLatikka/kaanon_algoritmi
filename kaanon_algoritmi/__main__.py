from sys import argv, exit
from time import sleep
from kaanon_algoritmi.logic.etsija import Etsija
from kaanon_algoritmi.globals import Globals
from kaanon_algoritmi.in_out.luku_ja_kirjoitus import LukuJaKirjoitus
from kaanon_algoritmi.in_out.muotoilu import Muotoilu


class Main:

    def __init__(self):
        self.etsija: Etsija = None

    def exec(self):
        try:
            Globals.version_ly = argv[3]
            self.get_nuottitiedoston_nimi()
            self.etsija = Etsija(LukuJaKirjoitus.lue_in())
            self.etsija.etsi()
            output: str = Muotoilu.get_output(self.etsija.loydetyt)
            LukuJaKirjoitus.kirjoita_out(output)
        except Exception as e:
            print("Unfortunately, an error did occur...\n\n")
            err_msg: str = Muotoilu.get_err_msg(str(e))
            LukuJaKirjoitus.kirjoita(LukuJaKirjoitus.polku_loki, err_msg, 'a')
            sleep(10)
            exit(1)

    def get_nuottitiedoston_nimi(self):
        tiedoston_nimi: str = input('\nNuottitiedoston nimi: ')
        print('\n')
        if tiedoston_nimi:
            Globals.nuottitiedoston_nimi = tiedoston_nimi
            return
        else:
            self.get_nuottitiedoston_nimi()


Main().exec()
