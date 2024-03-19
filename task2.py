fibonacci_nums = [1, 2]
while True:
    if fibonacci_nums[-1] >= 4*10**6:
        fibonacci_nums.pop(-1)
        break
    fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])

print(sum([num for num in fibonacci_nums if num%2==0]))


def gen_fibonacci(limit: int):
    num = 2
    prev_num = 1
    while prev_num < limit:
        yield prev_num
        prev_num, num = num, prev_num + num


print(sum([n for n in gen_fibonacci(4*10**6) if n % 2 == 0]))
