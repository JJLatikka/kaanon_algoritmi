from typing import Dict, List, Tuple
from fractions import Fraction


class Globals:
    version_ly: str

    nuottitiedoston_nimi: str

    dict_nuotit: Dict[str, int] = {'r': 0, 'c': 1, 'd': 3, 'e': 5, 'f': 6, 'g': 8, 'a': 10, 'b': 12}

    nuotit: List[str] = ["r", "c,,", "d,,", "e,,", "f,,", "g,,", "a,,", "b,,",
                         "c,", "d,", "e,", "f,", "g,", "a,", "b,",
                         "c", "d", "e", "f", "g", "a", "b",
                         "c'", "d'", "e'", "f'", "g'", "a'", "b'",
                         "c''", "d''", "e''", "f''", "g''", "a''", "b''",
                         "c'''", "d'''", "e'''", "f'''", "g'''", "a'''", "b'''"]

    tahtiosoitus: Tuple

    kaksijakoinen: bool

    tahtimaara: int

    soivia_distinct: int

    yksikko: Fraction

    jaollisuus: Fraction

    dissonanssit: List[int] = [1, 2, 6, 11]
