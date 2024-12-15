import app


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x * y

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or                                                not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(4, 2)
    print(result)
