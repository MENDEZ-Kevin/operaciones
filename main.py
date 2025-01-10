class Primo:
    def __init__(self, limite):
        self.limite = limite

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def obtener_primos(self):
        primos = []
        for num in range(2, self.limite + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos

# Ejemplo de uso:
limite = int(input("Ingrese un número límite: "))
calculadora = Primo(limite)
primos = calculadora.obtener_primos()

print(f"Los números primos hasta {limite} son: {primos}")
