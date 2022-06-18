class Conversor():

    def __init__(self):
        self.listBases =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def __toDecimal(self,text, base):
        j = 0
        if self.__validateToDecimal(text, base):
            sum = 0;
            for i in reversed(text):
                value = self.listBases.index(i)
                sum += value * (base ** j)
                j += 1
            return str(sum)
        else:
            raise Exception(f'El número: {text} no se encuentra en base: {base}')

    def __validateToDecimal(self, text, base):
        a = self.listBases[:base]
        for i in text:
            if not i in a:
                return False
        return True

    def __toBase(self, decimal, base):
        value = int(decimal);
        result = ""
        validate = True
        rest = 0
        quotient = 0
        while validate:
            quotient = value // base
            rest = value - (quotient * base)
            result += self.listBases[rest]
            value = quotient
            validate = value >= base
        if quotient > 0:
            result += self.listBases[quotient]
        return result[::-1]

    def baseTobase(self, number, baseInitial, baseFinal):
        try:
            self.__validateBases(baseInitial, baseFinal)
            print(f'base 10: {self.__toDecimal(number, baseInitial)}')
            return self.__toBase(self.__toDecimal(number, baseInitial), baseFinal)
        except Exception as e:
            return e

    def __validateBases(self, base1, base2):
        if base1 < 2 or base1 > len(self.listBases):
            raise Exception(f'La base: {base1}, no se encuentra comprendida entre 2 y {len(self.listBases)}')
        if base2 <= 1 or base2 > len(self.listBases):
            raise Exception(f'La base: {base2}, no se encuentra comprendida entre 2 y {len(self.listBases)}')