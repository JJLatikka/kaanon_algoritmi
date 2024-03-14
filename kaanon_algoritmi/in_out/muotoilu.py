from typing import List, Tuple
from datetime import datetime
from kaanon_algoritmi.globals import Globals


class Muotoilu:
    treble_ala: bool

    @classmethod
    def savelet_str(cls, arr: List) -> str:
        return '\n\t\t'.join(list(map(repr, arr)))

    @classmethod
    def matriisi_str(cls, arr: List[List]) -> str:
        return '\n\t\t'.join(list(map(lambda a: '-'.join(list(map(lambda s: s.nimi, a))), arr)))

    @classmethod
    def get_output(cls, loydetyt: List[Tuple[List, List]]) -> str:
        str_lilypond_rivit: List = [f'\\version "{Globals.version_ly}"\n']

        def get_treble(rivi: List) -> bool:
            return ''.join(set([s.nimi for s in rivi])).count("'") / Globals.soivia_distinct > 0.5

        cls.treble_ala: bool = get_treble(loydetyt[0][0])

        def rivi_str(rivi: List) -> str:
            return ' '.join([f'{str(s)}' for s in rivi])

        for i in range(len(loydetyt)):
            rivi = loydetyt[i][1]
            yla: str = rivi_str(rivi)
            treble_yla: bool = get_treble(rivi)
            ala: str = rivi_str(loydetyt[i][0])
            stemmat: str = cls.get_stemmat(yla, ala, treble_yla)
            str_lilypond_rivit += [stemmat]

        return '\n'.join(str_lilypond_rivit)

    @classmethod
    def get_stemmat(cls, yla: str, ala: str, treble_yla: bool):
        def get_clef(b: bool) -> str:
            return 'treble' if b else 'bass'

        def set_nuotit():
            return ['\\new PianoStaff <<',
                    '\\new Staff {',
                    f'\\clef {get_clef(treble_yla)}',
                    '\\key c \\major',
                    f'\\time {Globals.tahtiosoitus[0]}/{Globals.tahtiosoitus[1]}',
                    '{',
                    yla,
                    '}',
                    '}',
                    '\\new Staff {',
                    f'\\clef {get_clef(cls.treble_ala)}',
                    '\\key c \\major',
                    f'\\time {Globals.tahtiosoitus[0]}/{Globals.tahtiosoitus[1]}',
                    '{',
                    ala,
                    '}',
                    '}',
                    '>>']

        return '\n'.join(set_nuotit())

    @classmethod
    def get_err_msg(cls, str_err: str) -> str:
        return f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {str_err}\n'
