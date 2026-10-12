n = int(input())

def FindPrimeNumbers(n):
    numbers = set(range(2, n + 1))
    p = 2
    
    while p <= n:
        for i in range(2 * p, n + 1, p):
            numbers.discard(i)
        
        next_p = [x for x in sorted(numbers) if x > p]
        
        if next_p:
            p = next_p[0] 
        else:
            break 
            
    return sorted(numbers)

print(f"Найденные простые числа в диапазоне:", FindPrimeNumbers(n))
