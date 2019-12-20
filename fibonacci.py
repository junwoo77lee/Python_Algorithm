# Uses python3
# Problem description
# n is a single integer; 0 ≤ n ≤ 45

# # Naive algorithm
# def calc_fib(n):
#     if (n <= 1):
#         return n
#     return calc_fib(n - 1) + calc_fib(n - 2)

# Efficient algorithm
def fib_list(n):
    l = []
    for _ in range(n+1):
        if _ <= 1:
            l.append(_)
        else:
            l[0], l[1] = l[1], l[0] + l[1]
    return l[1] if n > 1 else l[n]


if __name__ == '__main__':
    n = int(input())
    print(fib_list(n))
