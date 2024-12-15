import app


class InvalidPermissions(Exception):
    pass

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x / y  # suma
        
    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise ValueError("ERROR HTTP 406")  # Cambié TypeError a ValueError
        return x / y

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

if __name__ == "__main__":  # testeo que sin las barras bajas no de error
    calc = Calculator()
    result = calc.add(4, 0)
    print(result)
