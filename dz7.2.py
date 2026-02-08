def safe_calculator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except Exception as e:
            print(f"Помилка: {type(e).__name__} – {e}")
            return None
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

print(calculate("2 + 3 * 4"))
print(calculate("10 / 0"))
print(calculate("abc + 5"))