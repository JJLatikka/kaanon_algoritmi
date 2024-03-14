import numpy as n
from typing import List, Tuple
from fractions import Fraction
from kaanon_algoritmi.domain.melodia import Melodia
from kaanon_algoritmi.logic.matriisi import Matriisi
from kaanon_algoritmi.domain.savel import Savel
from kaanon_algoritmi.globals import Globals
from kaanon_algoritmi.domain.kaanon import Kaanon


class Etsija:

    def __init__(self, melodia: str):
        self.melodia: Melodia = Melodia(melodia)
        self.matriisi: Matriisi = Matriisi(self.melodia.savelet)
        self.vaihe: int = 1
        self.vaihe_max: Fraction = self.set_vaihe_max()
        self.loydetyt: List[Tuple[List[Savel], List[Savel]]] = []

    @staticmethod
    def set_vaihe_max() -> Fraction:
        b: bool = Globals.tahtiosoitus[0] % 2 == 0
        tahteja: int | float = Globals.tahtimaara / 2 if b else Globals.tahtimaara // 2
        return Fraction(Globals.tahtiosoitus[0], Globals.tahtiosoitus[1]) * tahteja

    def etsi(self):
        while Globals.yksikko * self.vaihe <= self.vaihe_max:
            savelet: List[Savel] = self.matriisi.kloonaa(self.melodia.savelet)
            savelet: List[Savel] = self.vaiheista([savelet], 1, self.vaihe)
            for vastasavelet in self.matriisi.matriisi:
                vastasavelet: List[Savel] = self.vaiheista([vastasavelet], 0, self.vaihe)
                k: Kaanon = Kaanon(savelet, vastasavelet)
                if k.is_kaanon: self.loydetyt.append((savelet, vastasavelet))
            self.vaihe += 1

    def vaiheista(self, l_2d: List[List[Savel]], indeksi: int, maara: int) -> List[Savel]:
        l_2d.insert(indeksi, [Savel(s, Globals.yksikko) for s in 'r' * maara])
        return self.set_savelten_alkuhetket(n.concatenate(l_2d))

    def set_savelten_alkuhetket(self, savelet: List[Savel], t=Fraction(0)) -> List[Savel]:
        for s in savelet:
            s.alkuhetki = t
            t += s.kesto
        return savelet
