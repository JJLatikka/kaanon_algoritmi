from os import getcwd, path
from typing import Optional
from kaanon_algoritmi.in_out.muotoilu import Muotoilu
from kaanon_algoritmi.globals import Globals


class LukuJaKirjoitus:
    polku_in = path.join(getcwd(), 'input')
    polku_out = path.join(getcwd(), 'output', 'ly')
    polku_loki = path.join(getcwd(), 'output', 'loki', 'virheloki.txt')

    @classmethod
    def lue_in(cls) -> Optional[str]:
        try:
            with open(cls.get_polku(cls.polku_in, '.txt'), 'r') as tiedosto:
                return ''.join([rivi.strip() for rivi in tiedosto])
        except Exception as e:
            err_msg: str = Muotoilu.get_err_msg(str(e))
            cls.kirjoita(cls.polku_loki, err_msg, 'a')
            return None

    @classmethod
    def get_polku(cls, polku: str, paate: str) -> str:
        return path.join(polku, Globals.nuottitiedoston_nimi + paate)

    @classmethod
    def kirjoita_out(cls, output: str):
        cls.kirjoita(cls.get_polku(cls.polku_out, '.ly'), output)
        cls.kirjoita(path.join(cls.polku_out, 'kaanon_temp.txt'), Globals.nuottitiedoston_nimi)

    @classmethod
    def kirjoita(cls, polku: str, output: str, mode: str = 'w'):
        with open(polku, mode) as tiedosto:
            tiedosto.write(output)
