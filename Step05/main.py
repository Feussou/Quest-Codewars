def square_digits(num):
    result = "".join(str(int(i)**2) for i in str(num))
    return int(result)

#La logique est de prendre chaque chiffre 1 à 1 et de les mettres au carrés en utilisant .join
#pour regroupé les différents résulats pour la suite de caractères.