def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def do(n):
    return f"Performing the parameterized decorator with {n}"

# Call the decorated function and print the results
results = do(8)
print(results)
