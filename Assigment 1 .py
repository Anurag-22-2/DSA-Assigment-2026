def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


# fib naive 

def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

print("Naive Fibonacci(6):", fib_naive(6))





#Fib memo



memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print("Memoized Fibonacci(6):", fib_memo(6))




#  tower of hanoi


def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3, 'A', 'C', 'B')




#binary search


def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

data = [1, 3, 5, 7, 9, 11]

print("Index of 7:", binary_search(data, 0, len(data) - 1, 7))
