import re
from fractions import Fraction
from typing import Optional
from kaanon_algoritmi.globals import Globals


class Savel:

    def __init__(self, nimi: str, kesto: Fraction, sidottu: bool = False):
        self.nimi: str = nimi
        self.luku: int = self.set_luku(nimi)
        self.kesto: Fraction = kesto
        self.sidottu: bool = sidottu
        self.alkuhetki: Optional[Fraction] = None

    def set_luku(self, savel: str) -> int:
        return Globals.dict_nuotit[re.sub("[',]*", "", savel)]

    def __repr__(self) -> str:
        return (f'Savel{{ [nimi: {self.nimi:>3}] [luku: {self.luku:>2}] [kesto: {str(self.kesto):>5}] '
                f'[sidottu: {str(self.sidottu):>6}] [alkuhetki: {str(self.alkuhetki):>6}] }}')

    def __str__(self) -> str:
        def str_kesto() -> str:
            kaari: str = '~' if self.sidottu else ''
            return f'{self.kesto.denominator}' + kaari

        return f'{self.nimi}{str_kesto()}'
