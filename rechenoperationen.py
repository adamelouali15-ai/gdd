def addition(a: float, b: float) -> float:
    return a + b

def subtraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float | None:
    if b == 0:
        print("Division durch 0 nicht erlaubt!")
        return None
    return a / b



