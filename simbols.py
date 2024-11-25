class variable:
    def __init__(self, name, value, order = 1):
        self.name = name
        self.value = value
        self.order = order
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

    def evaluar(self):
        return self.value**self.order


class ecuacion:
    def __init__(self, coef_Vandermonde, y):
        self.coef_Vandermonde = coef_Vandermonde
        self.coef = []
        self.polinomio = None
        self.ye = y

        self.crear_quis()
    def __str__(self):
        return self.polinomio

    def __repr__(self):
        return self.polinomio

    def crear_quis(self):
        var = []
        for i in range(len(self.coef_Vandermonde)):
            if i != 0:
                var.append(variable(f"x^{i}", None, i))
            
        self.coef = var

        self.polinomio = self.crear_polinomio()

    def crear_polinomio(self):
        polinomio = ""
        
        for i in range(len(self.coef_Vandermonde)):
            if i == 0:
                polinomio += f"{self.coef_Vandermonde[i][0]} + "
            else:
                polinomio += f"{self.coef_Vandermonde[i][0]}*{self.coef[i-1]} + "

        polinomio = polinomio[:-2]
    
        return polinomio
    
    def evaluar(self, vectorye):
        for k in range(len(self.coef_Vandermonde)) :   
            y = 0
            for i in range(len(self.coef_Vandermonde)):
                if i == 0:
                    y += self.coef_Vandermonde[i][0]

                else:
                    self.coef[i-1].value = vectorye[k]
                    y += self.coef_Vandermonde[i][0] * self.coef[i-1].evaluar()

            print(f"P({vectorye[k]}) = {y}")