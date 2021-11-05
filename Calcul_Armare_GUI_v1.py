import tkinter as tk
from tkinter import filedialog as fd
import Calcul_Armare_v3 as CA
import Armare_to_Excel as A2E
import os
import pickle

tip_bara = ""


root = tk.Tk()


proiect = CA.start_proiect()


def get_tip_bara(tip_bara):
    return tip_bara


label_nume_grinda = tk.Label(root, text="Nume Grinda")
label_diam = tk.Label(root, text="Diametru Bara")
label_lung = tk.Label(root, text="Lungime Bara")
label_buc = tk.Label(root, text="Bucati Bara")

input_nume_grinda = tk.Entry(root, width=20)
input_diam = tk.Entry(root, width=20)
input_buc = tk.Entry(root, width=20)
input_lung = tk.Entry(root, width=25)

label_nume_grinda.grid(row = 0, column = 0, columnspan = 2)
input_nume_grinda.grid(row = 1, column = 0, columnspan = 2)


label_diam.grid(row = 0, column = 2, columnspan = 2)
input_diam.grid(row = 1, column = 2, columnspan = 2)


label_buc.grid(row = 0, column = 4, columnspan = 2)
input_buc.grid(row =1, column = 4, columnspan = 2)


label_lung.grid(row = 0, column = 6, columnspan = 4)
input_lung.grid(row= 1, column = 6, columnspan = 4)

# define tip bara dropdown
options = ["bara dreapta", "bara cu un cioc", "bara cu doua ciocuri", "etrier", "agrafa"]
clicked = tk.StringVar()
clicked.set("Tip de bara")
drop = tk.OptionMenu(root, clicked, *options)
drop.grid(row = 2, column = 0, columnspan = 2)


def get_info_from_GUI():
    nume_grinda = input_nume_grinda.get().lower()
    diametru = input_diam.get()
    tip_bara_value = clicked.get()
    lungime = input_lung.get()
    bucati = input_buc.get()
    if nume_grinda == "" and tip_bara_value == "" and lungime == "" and bucati == "" and diametru == "":
        pass
    else:
        return [int(diametru), float(lungime), tip_bara_value, int(bucati), nume_grinda]


def delete_info():
    #input_nume_grinda.delete(0, tk.END)
    input_diam.delete(0, tk.END)
    input_lung.delete(0, tk.END)
    input_buc.delete(0, tk.END)

def deduct_pcs():
    if get_info_from_GUI() == None:
        pass
    else:
        CA.remove_elem(get_info_from_GUI()[0], get_info_from_GUI()[1], get_info_from_GUI()[2], get_info_from_GUI()[3],
                    get_info_from_GUI()[4], proiect)

        for item in proiect.dict_grinzi_si_bare.keys():
            if get_info_from_GUI()[4] == item:
                for elem in proiect.dict_grinzi_si_bare[item]:
                    if get_info_from_GUI()[0] == elem.diam and get_info_from_GUI()[1] == elem.lung and \
                            get_info_from_GUI()[2] == elem.forma:
                        new_label_grinda_nume = tk.Label(root, text="Nume Grinda")
                        new_label_marca_nume = tk.Label(root, text="Marca")
                        new_label_diam_nume = tk.Label(root, text="Diametru")
                        new_label_buc_nume = tk.Label(root, text="Bucati")
                        new_label_lung_nume = tk.Label(root, text="Lungime")

                        new_label_grinda_nume.grid(row=3, column=0, columnspan=2)
                        new_label_marca_nume.grid(row=3, column=2, columnspan=2)
                        new_label_diam_nume.grid(row=3, column=4, columnspan=2)
                        new_label_buc_nume.grid(row=3, column=6, columnspan=2)
                        new_label_lung_nume.grid(row=3, column=8, columnspan=2)

                        new_label_grinda = tk.Label(root, text="Grinda " + elem.grinda.capitalize())
                        new_label_marca = tk.Label(root, text=elem.marca)
                        new_label_diam = tk.Label(root, text=elem.diam)
                        new_label_buc = tk.Label(root, text=elem.buc)
                        new_label_lung = tk.Label(root, text=elem.lung)

                        new_label_grinda.grid(row=4, column=0, columnspan=2)
                        new_label_marca.grid(row=4, column=2, columnspan=2)
                        new_label_diam.grid(row=4, column=4, columnspan=2)
                        new_label_buc.grid(row=4, column=6, columnspan=2)
                        new_label_lung.grid(row=4, column=8, columnspan=2)

    delete_info()


def display_one_elem():
    if get_info_from_GUI() == None:
        pass
    else:
        CA.add_elem(get_info_from_GUI()[0], get_info_from_GUI()[1], get_info_from_GUI()[2], get_info_from_GUI()[3],
                    get_info_from_GUI()[4], proiect)
        for item in proiect.dict_grinzi_si_bare.keys():
            if get_info_from_GUI()[4] == item:
                for elem in proiect.dict_grinzi_si_bare[item]:
                    if get_info_from_GUI()[0] == elem.diam and get_info_from_GUI()[1] == elem.lung and \
                            get_info_from_GUI()[2] == elem.forma:

                        new_label_grinda_nume = tk.Label(root, text="Nume Grinda")
                        new_label_marca_nume = tk.Label(root, text="Marca")
                        new_label_diam_nume = tk.Label(root, text="Diametru")
                        new_label_buc_nume = tk.Label(root, text="Bucati")
                        new_label_lung_nume = tk.Label(root, text="Lungime")

                        new_label_grinda_nume.grid(row = 3, column = 0, columnspan = 2)
                        new_label_marca_nume.grid(row = 3, column = 2, columnspan = 2)
                        new_label_diam_nume.grid(row = 3, column = 4, columnspan = 2)
                        new_label_buc_nume.grid(row = 3, column = 6, columnspan = 2)
                        new_label_lung_nume.grid(row = 3, column = 8, columnspan = 2)

                        new_label_grinda = tk.Label(root, text="Grinda " + elem.grinda.capitalize())
                        new_label_marca = tk.Label(root, text=elem.marca)
                        new_label_diam = tk.Label(root, text=elem.diam)
                        new_label_buc = tk.Label(root, text=elem.buc)
                        new_label_lung = tk.Label(root, text=elem.lung)

                        new_label_grinda.grid(row = 4, column = 0, columnspan = 2)
                        new_label_marca.grid(row = 4, column = 2, columnspan = 2)
                        new_label_diam.grid(row = 4, column = 4, columnspan = 2)
                        new_label_buc.grid(row = 4, column = 6, columnspan = 2)
                        new_label_lung.grid(row = 4, column = 8, columnspan = 2)

    delete_info()


def display_info():
    #print(CA.dict_grinzi)
    new_label_grinda_nume = tk.Label(root, text="Nume Grinda")
    new_label_diam_nume = tk.Label(root, text="Diametru")
    new_label_lung_nume = tk.Label(root, text="Lungime")
    new_label_buc_nume = tk.Label(root, text="Bucati")
    new_label_marca_nume = tk.Label(root, text="Marca")

    new_label_grinda_nume.grid(row=3, column=0, columnspan = 2)
    new_label_marca_nume.grid(row=3, column=2, columnspan = 2)
    new_label_diam_nume.grid(row=3, column=4, columnspan = 2)
    new_label_buc_nume.grid(row=3, column=6, columnspan=2)
    new_label_lung_nume.grid(row=3, column=8, columnspan = 2)

    value = 0
    for item in proiect.dict_grinzi_si_bare.keys():

        for elem in proiect.dict_grinzi_si_bare[item]:
            value += 1
            #grinda_name = str(elem.grinda).capitalize()
            new_label_grinda_final = tk.Label(root, text = "Grinda " + elem.grinda.capitalize())
            new_label_diam_final = tk.Label(root,text= elem.diam)
            new_label_lung_final = tk.Label(root, text = elem.lung)
            new_label_buc_final = tk.Label(root, text = elem.buc)
            new_label_marca_final = tk.Label(root, text = elem.marca)

            new_label_grinda_final.grid(row=value + 3, column=0, columnspan = 2)
            new_label_marca_final.grid(row=value + 3, column=2, columnspan = 2)
            new_label_diam_final.grid(row=value + 3, column=4, columnspan = 2)
            new_label_buc_final.grid(row=value + 3, column=6, columnspan=2)
            new_label_lung_final.grid(row=value + 3, column=8, columnspan = 2)


def print_to_excel(proiect):
    file = fd.askdirectory()
    A2E.print_to_excel(proiect, file)


def export(proiect):
    file = fd.askdirectory()
    with open(file + "/1. export_toate_barele.txt", "wb") as export_toate_barele:
        pickle.dump(proiect.lista_toate_barele, export_toate_barele)
    with open(file + "/2. export_bare_unice.txt", "wb") as export_bare_unice:
        pickle.dump(proiect.lista_bare_unice, export_bare_unice)
    with open(file + "/3. export_dict_grinzi.txt", "wb") as export_bare:
        pickle.dump(proiect.dict_grinzi_si_bare, export_bare)



def import_dict_grinzi(filename):
    dict_bare_pickle = open(filename, "rb")
    proiect.dict_grinzi_si_bare = pickle.load(dict_bare_pickle)
    return proiect.dict_grinzi_si_bare


def import_toate_barele(filename):
    dict_bare_pickle = open(filename, "rb")
    proiect.lista_toate_barele = pickle.load(dict_bare_pickle)
    return proiect.lista_toate_barele


def import_bare_unice(filename):
    dict_bare_pickle = open(filename, "rb")
    proiect.lista_bare_unice = pickle.load(dict_bare_pickle)
    return proiect.lista_bare_unice


def import_bare():
    filename = fd.askopenfilenames()
    import_bare_unice(filename[1])
    import_dict_grinzi(filename[2])
    import_toate_barele(filename[0])


buton_adauga = tk.Button(root, text = "Adauga Bara", command = display_one_elem)
buton_scade = tk.Button(root, text = "Scade Bucati", command = deduct_pcs)
buton_afisare = tk.Button(root, text = "Afisare Bare", command = display_info)
buton_excel = tk.Button(root, text = "Catre Excel", command = lambda: print_to_excel(proiect))
buton_export = tk.Button(root, text = "Export info", command = lambda: export(proiect))
buton_import = tk.Button(root, text = "Import info", command = lambda: import_bare())


buton_adauga.grid(row = 0, column = 10)
buton_scade.grid(row = 0, column = 11)
buton_afisare.grid(row = 0, column = 12)
buton_excel.grid(row = 1, column = 10)
buton_export.grid(row = 1, column = 11)
buton_import.grid(row = 1, column = 12)


root.mainloop()

