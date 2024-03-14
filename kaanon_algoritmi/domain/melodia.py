import re
import numpy as n
from typing import List
from fractions import Fraction
from kaanon_algoritmi.domain.savel import Savel
from kaanon_algoritmi.globals import Globals
from kaanon_algoritmi.in_out.muotoilu import Muotoilu


class Melodia:

    def __init__(self, melodia: str):
        self.osat: List[str] = self.set_osat(melodia)
        self.savelet: List[Savel] = self.set_savelet()
        self.additional_settings()
        self.pitkat_savelet()

    def set_osat(self, melodia: str) -> List[str]:
        return [o.strip() for o in melodia.split('|')]

    def set_savelet(self) -> List[Savel]:
        return list(map(self.get_savel_uusi, n.concatenate([o.split(" ") for o in self.osat[1:]])))

    def get_savel_uusi(self, savel: str) -> Savel:
        return Savel(self.get_nimi(savel), self.get_kesto(savel))

    def get_nimi(self, savel: str) -> str:
        return re.sub("\\d|[.]*", "", savel)

    def get_kesto(self, savel: str) -> Fraction:
        numero_osa = int(re.sub("[a-z]|[',.]*", "", savel))
        return self.get_murtoluku(numero_osa, savel.count('.'))

    def get_murtoluku(self, numero_osa: int, pisteet: int, pidennys: Fraction = 0) -> Fraction:
        if pisteet:
            pidennys: Fraction = self.get_pidennys(numero_osa, pisteet)
        return Fraction(1, numero_osa) + pidennys

    def get_pidennys(self, numero_osa: int, pisteet: int, pidennys: Fraction = 0):
        while pisteet > 0:
            numero_osa *= 2
            pidennys += Fraction(1, numero_osa)
            pisteet -= 1
        return pidennys

    def additional_settings(self):
        o: List[str] = self.osat[0].split('/')
        Globals.tahtiosoitus = (int(o[0]), int(o[1]))
        Globals.yksikko = Fraction(1, Globals.tahtiosoitus[1])
        Globals.kaksijakoinen = Globals.tahtiosoitus[0] % 3 != 0
        Globals.jaollisuus = Fraction(2 if Globals.kaksijakoinen else 3, Globals.tahtiosoitus[1])
        Globals.tahtimaara = len(self.osat) - 1
        Globals.soivia_distinct = len(set([s.nimi for s in self.savelet if s.nimi != 'r']))

    def pitkat_savelet(self):
        for i in range(len(self.savelet)):
            s: Savel = self.savelet[i]
            if s.kesto > Globals.yksikko:
                yksikkoja: int = s.kesto // Globals.yksikko
                jaannos: Fraction = s.kesto - yksikkoja * Globals.yksikko
                self.lyhyempia_tilalle(i, yksikkoja, jaannos)
                self.pitkat_savelet()

    def lyhyempia_tilalle(self, i: int, yksikkoja: int, jaannos: Fraction):
        s: Savel = self.savelet.pop(i)
        while yksikkoja > 0:
            sidottu: bool = s.nimi != 'r' and (yksikkoja > 1 or jaannos > 0)
            self.savelet.insert(i, Savel(s.nimi, Globals.yksikko, sidottu))
            yksikkoja -= 1
            i += 1
        if jaannos:
            self.savelet.insert(i, Savel(s.nimi, jaannos, False))

    def __str__(self) -> str:
        return '\n'.join([
            f'\nMelodia: {{', f'\ttahtiosoitus:\t{self.osat[0]:>5}',
            f'\tkaksijakoinen:\t{str(Globals.kaksijakoinen):>5}',
            f'\ttahtimaara:\t\t{Globals.tahtimaara:>5}',
            f'\tsavelet: [\n\t\t{Muotoilu.savelet_str(self.savelet)}\n\t]\n}}'
        ])
