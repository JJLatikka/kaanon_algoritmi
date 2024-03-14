import numpy as n
from typing import Dict, List, Tuple
from kaanon_algoritmi.domain.savel import Savel
from kaanon_algoritmi.globals import Globals
from kaanon_algoritmi.in_out.muotoilu import Muotoilu


class Matriisi:

    def __init__(self, savelet: List[Savel]):
        self.dict_tr: Dict[str, int] = self.get_dict_tr(Globals.nuotit)
        self.perus: List[Savel] = self.kloonaa(savelet)
        self.krapu: List[Savel] = self.kaanteinen_jarjestys(self.perus)
        self.inver: List[Savel] = self.set_inversio(self.perus)
        self.krapuinver: List[Savel] = self.kaanteinen_jarjestys(self.inver)
        self.matriisi: List[List[Savel]] = self.set_matriisi()

    def get_dict_tr(self, lst: List[str]) -> Dict[str, int]:
        return {lst[i]: i for i in range(len(lst))}

    def kloonaa(self, savelet: List[Savel]) -> List[Savel]:
        return [Savel(s.nimi, s.kesto, s.sidottu) for s in savelet]

    def kaanteinen_jarjestys(self, savelet: List[Savel], indeksista: int = 0) -> List[Savel]:
        kaannettava: List[Savel] = self.kloonaa(savelet)
        kaarilista: List[bool] = [s.sidottu for s in kaannettava]

        def vaihda_kaarien_suunnat(indeksista: int):
            while indeksista < len(kaarilista) - 1:
                if True in kaarilista[indeksista:]:
                    i_alku: int = kaarilista.index(True, indeksista)
                    i_loppu: int = kaarilista.index(False, i_alku + 1)
                    s_alku, s_loppu = kaannettava[i_alku], kaannettava[i_loppu]
                    s_alku.sidottu, s_loppu.sidottu = False, True
                    indeksista = i_loppu + 1
                else:
                    return

        if True in kaarilista:
            vaihda_kaarien_suunnat(indeksista)
        return kaannettava[::-1]

    def set_inversio(self, savelet: List[Savel]) -> List[Savel]:
        tuplet_tr: List[Tuple[int, Savel]] = self.get_tuplet_tr(savelet)
        sym_i: int = self.get_symmetria_indeksi(tuplet_tr)
        return [self.get_savel_tr(sym_i + (sym_i - t[0]), t[1]) for t in tuplet_tr]

    def get_tuplet_tr(self, savelet: List[Savel]) -> List[Tuple[int, Savel]]:
        return [(self.dict_tr[s.nimi], s) for s in savelet]

    def get_symmetria_indeksi(self, tuplet_tr: List[Tuple[int, Savel]]) -> int:
        for t in tuplet_tr:
            if t[0] != 0: return t[0]

    def get_savel_tr(self, i: int, s: Savel) -> Savel:
        nimi: str = Globals.nuotit[i] if s.nimi != "r" else "r"
        return Savel(nimi, s.kesto, s.sidottu)

    def set_matriisi(self) -> List[List[Savel]]:
        return n.concatenate([self.get_list_tr(self.get_tuplet_tr(l)) for l in
                              [self.perus, self.krapu, self.inver, self.krapuinver]])

    def get_list_tr(self, tuplet_tr: List[Tuple[int, Savel]]) -> List[List[Savel]]:
        return [[self.get_savel_tr(t[0] + i, t[1]) for t in tuplet_tr] for i in range(7)]

    def __str__(self) -> str:
        return '\n'.join([
            f'\nMatriisi: {{'
            f'\n\tperusmuoto: [\n\t\t{Muotoilu.savelet_str(self.perus)}\n\t]',
            f'\n\tkrapuliike: [\n\t\t{Muotoilu.savelet_str(self.krapu)}\n\t]',
            f'\n\tinversio: [\n\t\t{Muotoilu.savelet_str(self.inver)}\n\t]',
            f'\n\tkrapuinversio: [\n\t\t{Muotoilu.savelet_str(self.krapuinver)}\n\t]'
            f'\n\n\tmatriisi: [\n\t\t{Muotoilu.matriisi_str(self.matriisi)}\n\t]\n}}'
        ])
