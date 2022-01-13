from math import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        self.coeffs=coeffs
        self.a=coeffs[2]
        self.b=coeffs[1]
        self.c=coeffs[0]
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        pass

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        self.a=self.a+other.a
        self.b=self.b+other.b
        self.c=self.c+other.c
        return f"{self.a}X^2 + ({self.b})X + ({self.c})"
    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        self.a=self.a-other.a
        self.b=self.b-other.b
        self.c=self.c-other.c
        return f"{self.a}X^2 + ({self.b})X + ({self.c})"
    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs)]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        return f"{self.coeffs[2]}X^2 + ({self.coeffs[1]})X + {self.coeffs[0]}"

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        c,b,a=self.coeffs
        
        # calculon delte
        
        delta= b**2-4*a*c
        if delta>0:
            #lequation admet deux solutions réelle
            x1=(-b-sqrt(delta))/(2*a)
            x2= x1=(-b+sqrt(delta))/(2*a)
            return f"({x1};{x2}"
        elif delta==0:
            x0=(-b)/(2*a)
            return f"({x0})"
        else :
            delta=-delta
            # deux solution imaginaire
            j1= complex(-b/(2*a),-sqrt(delta)/(2*a))
            j2=complex(-b/(2*a),sqrt(delta)/(2*a))
            return f"({j1};{j2}"
        

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        #assert isinstance(float,x),"donner un nombre reel"
        return self.coeffs[2]*(x**2)+self.coeffs[1]*x+self.coeffs[0]

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        
        x_points=list(range(0,21))
        y = list(map(self.__val,x_points))
        axes = plt.gca()
        plt.title(f"{self.coeffs[2]}X^2 + ({self.coeffs[1]})X + {self.coeffs[0]}")
        axes.grid(True)
        axes.set_xlabel('x : Abscisse')
        axes.set_ylabel('f(x) : Ordonnée')
        plt.plot(x_points, y,linestyle = 'dotted')
        plt.savefig("courbe.png")
        plt.show()


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
    
