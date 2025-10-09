class Solution(object):
    def addBinary(self, a, b):
        numbers_a = list(a)
        numbers_b = list(b)
        a_number = 0
        b_number = 0
        base = 1
        soma = []
        resto = []
        binary = 0

        for i in a[::-1]:
            if i == '1':
                a_number = a_number + base
                base = base * 2
            else:
                base = base * 2

        base = 1
        for i in b[::-1]:
            if i == '1':
                b_number = b_number + base
                base = base * 2
            else:
                base = base * 2
        
        soma = a_number + b_number
        if soma == 0:
            return '0'
        while(soma != 0):
            resto.append(soma % 2)
            soma = soma // 2
        resto = resto[::-1]
        binary = ("".join(map(str, resto)))
        return binary