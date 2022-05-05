import operator

def basic_op(operat, value1, value2):
    op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }
    return op[operat](value1, value2)

# la logique est d'atribuer a chaque opérateur, la fonction qui lui est attribuer 
# grâce à operator.add par exemple qui pour operateur.add(value1, value2) équivaut
# à value1+value2
