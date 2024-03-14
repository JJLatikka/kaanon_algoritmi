from fractions import Fraction
from typing import List, Optional
from math import fabs
from kaanon_algoritmi.domain.savel import Savel
from kaanon_algoritmi.globals import Globals


class Intervalli:

    def __init__(self, alkuhetki: Fraction, savelet: List[Savel]):
        self.alkuhetki: Fraction = alkuhetki
        self.koko: Optional[int] = self.set_intervallin_koko(savelet)
        self.konsonansi: bool = self.set_konsonanssi()

    def set_intervallin_koko(self, savelet: List[Savel]) -> Optional[int]:
        if len(savelet) < 2 or savelet[0].nimi == 'r' or savelet[1].nimi == 'r':
            return None
        return int(fabs(savelet[0].luku - savelet[1].luku))

    def set_konsonanssi(self) -> bool:
        return self.koko not in Globals.dissonanssit

    def __str__(self) -> str:
        return (f'Intervalli: {{alkuhetki: {str(self.alkuhetki):>6}, koko: {str(self.koko):>4}, '
                f'konsonanssi: {str(self.konsonansi):>5}}}')
