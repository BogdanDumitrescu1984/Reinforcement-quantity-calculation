import json
from json import JSONEncoder

class Proiect:
    def __init__(self):
        self.lista_toate_barele = []
        self.lista_bare_unice = []
        self.dict_grinzi_si_bare = {}


class Bara:
    def __init__(self, diam:int, lung:float, forma:str, marca:int = None, buc:int = None, grinda:str= None):
        self.diam = diam
        self.lung = lung
        self.forma = forma
        self.marca = marca
        self.buc = buc
        self.grinda = grinda
        self.lista_indici = []

    def add_bara(self, proiect: Proiect):
        proiect.lista_toate_barele.append(self)

    def __eq__(self, other):
        return self.diam == other.diam and self.lung == other.lung and self.forma == other.forma

    def add_bara_unica(self, proiect: Proiect):
        if len(proiect.lista_bare_unice) == 0:
            proiect.lista_bare_unice.append(self)
        else:
            for elem in proiect.lista_bare_unice:
                self.lista_indici.append(self == elem)

        if True not in self.lista_indici and len(self.lista_indici) != 0:
            proiect.lista_bare_unice.append(self)

    def add_marca(self, proiect):
        self.marca = proiect.lista_bare_unice.index(self)+1

    def set_grinda(self, grinda:str):
        self.grinda = grinda

    def _add_grinda_to_dict(self, proiect: Proiect):
        proiect.dict_grinzi_si_bare[self.grinda] = []

    def check_grinda_duplicate(self, proiect: Proiect):
        if len(proiect.dict_grinzi_si_bare) == 0:
            self._add_grinda_to_dict(proiect)
        else:
            if self.grinda not in proiect.dict_grinzi_si_bare.keys():
                self._add_grinda_to_dict(proiect)

    def add_bara_to_grinda(self, proiect):
        lista_indici = []
        if len(proiect.dict_grinzi_si_bare[self.grinda]) == 0:
            proiect.dict_grinzi_si_bare[self.grinda].append(self)
        else:
            for value in proiect.dict_grinzi_si_bare[self.grinda]:
                lista_indici.append(value.marca == self.marca)

            if True not in lista_indici:
                proiect.dict_grinzi_si_bare[self.grinda].append(self)

    def set_pcs_nr(self, buc:int):
        self.buc = buc

    def add_buc_if_bara_is_duplicate(self, proiect:Proiect):
        for value in proiect.dict_grinzi_si_bare[self.grinda]:
            if value.marca == self.marca and self is not value:
                value.buc += self.buc

    def deduct_pcs_if_bara_is_duplicate(self, proiect: Proiect):
        for value in proiect.dict_grinzi_si_bare[self.grinda]:
            if value.marca == self.marca and self is not value:
                value.buc -= self.buc

    def remove_bara_if_pcs_equal_zero(self, proiect: Proiect):
        for value in proiect.dict_grinzi_si_bare[self.grinda]:
            if value.buc == 0:
                proiect.dict_grinzi_si_bare[self.grinda].remove(value)
        for value in proiect.lista_bare_unice:
            if value.buc == 0:
                proiect.lista_bare_unice.remove(value)

    def update_marca(self, proiect: Proiect):
        if len(proiect.lista_bare_unice) != 0:
            for elem in proiect.lista_bare_unice:
                elem.marca = proiect.lista_bare_unice.index(elem)+1
        else:
            print("Nu sunt bare introduse")


def start_proiect():
    proiect = Proiect()
    return proiect


def add_elem(diam:int, lung:float, forma:str, buc:int, grinda:str, proiect: Proiect):
    bara = Bara(diam, lung, forma)
    bara.add_bara(proiect)
    bara.add_bara_unica(proiect)
    bara.add_marca(proiect)
    bara.set_grinda(grinda)
    bara.check_grinda_duplicate(proiect)
    bara.add_bara_to_grinda(proiect)
    bara.set_pcs_nr(buc)
    bara.add_buc_if_bara_is_duplicate(proiect)


def remove_elem(diam:int, lung:float, forma:str, buc:int, grinda:str, proiect: Proiect):
    bara = Bara(diam, lung, forma)
    bara.add_bara(proiect)
    bara.add_bara_unica(proiect)
    bara.add_marca(proiect)
    bara.set_grinda(grinda)
    bara.check_grinda_duplicate(proiect)
    bara.add_bara_to_grinda(proiect)
    bara.set_pcs_nr(buc)
    bara.deduct_pcs_if_bara_is_duplicate(proiect)
    bara.remove_bara_if_pcs_equal_zero(proiect)
    bara.update_marca(proiect)

class BaraEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def write_to_file(proiect):
    json_file = open("armare.json", "w")
    json.dump(proiect.dict_grinzi_si_bare, json_file, indent=2, cls=BaraEncoder)
    json_file.close()


def read_from_file(proiect):
    json_file = open("armare.json", "r")
    proiect.dict_grinzi_si_bare = json.load(json_file)
    print(proiect.dict_grinzi_si_bare)
    return proiect.dict_grinzi_si_bare





