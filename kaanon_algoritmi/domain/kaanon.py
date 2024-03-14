import numpy as n
from typing import List, Dict
from fractions import Fraction
from kaanon_algoritmi.domain.savel import Savel
from kaanon_algoritmi.domain.intervalli import Intervalli
from kaanon_algoritmi.globals import Globals


class Kaanon:

    def __init__(self, savelet: List[Savel], vastasavelet: List[Savel]):
        self.savelet: List[Savel] = savelet
        self.vastasavelet: List[Savel] = vastasavelet
        self.dict_yksikko: Dict[Fraction, List[Savel]] = {}
        self.intervallit: List[Intervalli] = self.set_intervallit()
        self.is_kaanon: bool = self.set_is_kaanon()

    def set_intervallit(self) -> List[Intervalli]:
        self.set_yksikko_dict(n.concatenate([self.savelet, self.vastasavelet]))
        return [Intervalli(k, self.dict_yksikko[k]) for k in self.dict_yksikko.keys()]

    def set_yksikko_dict(self, savelet: List[Savel]):
        for s in savelet:
            if s.alkuhetki % Globals.yksikko == 0:
                if s.alkuhetki not in self.dict_yksikko:
                    self.dict_yksikko[s.alkuhetki] = []
                self.dict_yksikko[s.alkuhetki].append(s)

    def set_is_kaanon(self) -> bool:
        for i in self.intervallit:
            if i.koko is None or i.alkuhetki % Globals.jaollisuus != 0:
                continue
            if not i.konsonansi: return False
        return True
