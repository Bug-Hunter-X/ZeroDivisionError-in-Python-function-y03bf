def function(a, b):
    if b == 0:
        return 0  # Or raise an exception: raise ZeroDivisionError("Division by zero")
    else:
        return a / b

result = function(10, 0)
print(result) # Output: 0
result = function(10,2)
print(result) # Output 5.0