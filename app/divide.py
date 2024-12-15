import app


class InvalidPermissions(Exception):
    pass


class Calculator:
    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("error HTTP 406")

        return x / y

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
