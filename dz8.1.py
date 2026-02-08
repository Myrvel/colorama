import logging
def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Помилка у {func.__name__}: {type(e).__name__} – {e}")
            return None
    return wrapper

@log_errors
def risky_function(x, y):
    return x / y

print(risky_function(10, 2))
print(risky_function(10, 0))