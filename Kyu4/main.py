def valid_solution(elplan):

    dec = {1, 2, 3, 4, 5, 6, 7, 8 ,9}
    for i in range(9):
        #Lignes
        if set(elplan[i]) != dec:
            return False
        #Colones
        if i == 0:
            for j in range(9):
                if set([elplan[x][j] for x in range(9)]) != dec:
                    return False
        #Carrés de 3
        if i in {0, 3, 6}:
            for j in [0, 3, 6]:
                if set(elplan[i][j : j + 3] + elplan[i + 1][j : j + 3] + elplan[i + 2][j : j + 3]) != dec:
                    return False
    return True

#Le code parcours le sudoku par lignes et par colones, et vérifie les carrés de 3 pour vérifié si les chiffres contenu
#dans le tableau de 9 par 9 ne se répéte pas sur la même ligne ou colones, et que le carrés de 3 par 3 contient chacun
#des chiffres contenu dans "dec" sois les entiers de 1 à 9.