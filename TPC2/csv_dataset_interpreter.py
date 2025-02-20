import re

from pprint import pprint
from dataclasses import dataclass
from sys import stdin

@dataclass
class MusicRecord:
    nome: str
    desc: str
    anoCriacao: int
    periodo: str
    compositor: str
    duracao: str
    _id: str

def generateDataset(plaincsv: str) -> set[MusicRecord]:
    res = list()

    matches = re.findall(r"[^ \n]+?(?:[^;]+;){6}[^\n]+", plaincsv)

    for i in range(1, len(matches)):
        elems = re.findall(r"[^;]+", matches[i])

        if len(elems) == 7:
            res.append(MusicRecord(elems[0],
                                   elems[1],
                                   elems[2],
                                   elems[3],
                                   elems[4],
                                   elems[5],
                                   elems[6]))

    return res

def composersInOrder(dataset: list[MusicRecord]) -> set[str]:
    res = set()

    for mr in dataset:
        res.add(mr.compositor)

    return sorted(res)

def musicCountByPeriod(dataset: list[MusicRecord]) -> dict[str, int]:
    res = dict()

    for mr in dataset:
        count = res.get(mr.periodo, 0)
        res[mr.periodo] = count + 1

    return res

def musicByPeriod(dataset: list[MusicRecord]) -> dict[str, int]:
    res = dict()

    for mr in dataset:
        mbp = res.get(mr.periodo, [])
        mbp.append(mr.nome)
        res[mr.periodo] = mbp

    for names in res.values():
        names.sort()

    return res

def main():
    plaincsv = open('obras.csv', 'r', encoding='utf-8').read()
    dataset = generateDataset(plaincsv)
    print("Lista ordenada alfabeticamente dos compositores musicais:")
    pprint(composersInOrder(dataset))
    print("\n")

    print("Obras catalogadas em cada período:")
    pprint(musicCountByPeriod(dataset))
    print("\n")

    print("Lista alfabética dos títulos das obras de cada período:")
    pprint(musicByPeriod(dataset))
    print("\n")


if __name__ == "__main__":
    main()
