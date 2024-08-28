class Complex:
    def __init__(self,re,im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im == 0:
            return f"{self.re}"
        elif self.im < 0:
            if self.im == -1:
                return f"{self.re}-i"
            return f"{self.re}-{-self.im}i"
        elif self.im in [0,1]:
            return f"{self.re}+i"
        else:
            return f"{self.re}+{self.im}i"

    def somme(self,other):
        return f"{self.re + other.re}+{self.im + other.im}i"

    def produit(self,other):
        nvRe = self.re * other.re - self.im * other.im
        nvIm = self.im * other.re + self.re * other.im
        return Complex(nvRe,nvIm)

    def conjugue(self):
        return f"{self.re}-{self.im}i"

    def module(self):
        return (self.re**2 + self.im**2)**(1/2)

    def carre(self):
        return self.re**2 - self.im**2

    def comparaison(self,other):
        if self.re > other.re:
            return f"({self}) > ({other})"
        elif self.re == other.re:
            if self.im <= other.im:
                return f"({self}) > ({other})"
            else:
                return f"({self}) < ({other})"
        else:
            return f"({self}) < ({other})"

x = Complex(1,3)
y = Complex(3,2)
print(x)
print(y)

