def generate_fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = generate_fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def generate_fibonacci_iterative(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

def calculate_fibonacci_sum(sequence):
    return sum(sequence)

if __name__ == "__main__":
    n_terms = int(input("Enter the number of Fibonacci terms to generate: "))

    recursive_sequence = generate_fibonacci_recursive(n_terms)
    iterative_sequence = generate_fibonacci_iterative(n_terms)

    print("Fibonacci sequence (recursive method):", recursive_sequence)
    print("Fibonacci sequence (iterative method):", iterative_sequence)

    recursive_sum = calculate_fibonacci_sum(recursive_sequence)
    iterative_sum = calculate_fibonacci_sum(iterative_sequence)

    print("Sum of Fibonacci sequence (recursive method):", recursive_sum)
    print("Sum of Fibonacci sequence (iterative method):", iterative_sum)
