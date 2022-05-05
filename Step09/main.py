def tribonacci(signature, n):
    i = 0
    if n != 0: 
        
        while len(signature) < n:
            signature.append(signature[i] + signature[i+1] + signature[i+2])
            i += 1
        signature = signature[0:n]
        return signature
    return []

#On cherche ici à continuer la suite de tribonacci, en utilisant .append afin d'ajouter à 
#signature les variables nécessaires tant que la longueur de la liste est inférieure à n. 
#Si n n'est pas égal à 0, alors la fonction ne renvoie rien.