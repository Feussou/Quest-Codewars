def score(dice):
    score = 0
    for i in range(1, 7): 
        total = dice.count(i)
        if total >= 3:
            score += i * (1000 if i == 1 else 100)
            total -= 3
        if i in [1, 5]:
            score += total * 50 * (2 if i == 1 else 1)
    return score

#On sait qu'il y à 2 type de score, les triplés et les simples, en fonction de ça on va
#mltiplié par 1000 ou 100 en fonction des chiffres obtenu sur les dés.