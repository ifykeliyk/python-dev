def gen_primes(start, end):
    for num in range(start, end+1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


list = list(gen_primes(50, 100))
print(list)

for value in gen_primes(50, 100):
    if value % 10 == 7:
        print(value)
        break


for value in gen_primes(50, 100):
    if value % 10 == 1:
        print(value)
        break


def gen_countdown(n):
    while n > 0:
        yield n
        n -= 1


for num in gen_countdown(5):
    print(num)
