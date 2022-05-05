def is_triangle(a, b, c):
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False

#Le théorème de l'inégalité triangulaire
# établit que l'addition des longueurs de deux côtés 
# d'un triangle est toujours supérieure à celle du troisième côté.
#il suffit alors de vérifier que deux côtés sont supérieur au côté restant, 3 fois.