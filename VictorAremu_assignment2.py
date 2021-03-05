# Victor Aremu
# Assignment 2

# Fibonacci series
# where a user specifies the length of the fibonacci series
#Assignment 1

def fib(fib_len):
    fib_len = int(input("Enter the size of the fibonacci series: "))
    num = 0
    list_fib = [0, 1]
    while len(list_fib) < fib_len:
        third_num = list_fib[num] + list_fib[num+1]
        list_fib.append(third_num)
        num += 1
    print(list_fib)

fib()

