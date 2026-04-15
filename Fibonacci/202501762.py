def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    
    sequence = []
    a, b = 0, 1
    
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

num = int(input("Enter a number: "))

print("Fibonacci sequence:", fibonacci(num))