def solution(n):
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    rom = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i = 12  
    rom_num = ''
    while n != 0:
        if num[i] <= n:    
            rom_num += rom[i] 
            n = n - num[i]
        else:
            i -= 1 # i = i - 1
    return rom_num

#Pour cet exercice il s'agit d'attribuer a chaque valeur numérique "num" une valeur romaine
#"rom", i représente alors le nombre de possibilité,
#la bouble vérifie alors si le chiffre correspond au paramètre n et si non le réduit a l'inférieur 
#jusqu'a ce que le résultat de n = n - num soit égal à 1.
