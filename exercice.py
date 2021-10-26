#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
def compareFichier(nom_fichier_reference, nom_fichier_a_comparer):
    with open(nom_fichier_reference) as r:
        list_lines_r = r.readlines()
        if len(list_lines_r) == 0:
            return "premier fichier est vide"
        with open(nom_fichier_a_comparer) as c:
            list_lines_c = c.readlines()
            if len(list_lines_c) == 0:
                return "deuxième fichier est vide"

            for i in range(len(list_lines_r)):
                for j in range(len(list_lines_r[i])):
                     if list_lines_r[i][j] != list_lines_c[i][j]:
                         return f"différence à la position {i}, {j}"
                     else:
                         return "Aucune différence"

# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(compareFichier("./exemple.txt", "./exemple2"))
    pass
