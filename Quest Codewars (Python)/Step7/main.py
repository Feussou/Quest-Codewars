def in_asc_order(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]: 
            return False
    return True

#Le code verifie si le chiffre est plus ou moins grand que le chiffre qui viens après lui dans
#la liste