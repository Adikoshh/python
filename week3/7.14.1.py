def countDivisors(a):
    result = []
    i = 1
    while i * i < a + 1:
        if a % i == 0:
            result.append(i)
            if i != a // i:
                result.append(a // i)
        i += 1
    return sorted(result)


def function(m, n):
    div = []
    for num in range(m, n + 1):
        frac = countDivisors(num)
        div.append((len(frac), -num, frac[-2:]))
    div.sort()
    print(-div[-1][1], 'consist', div[-1][0], 'divisors')


function(2, 4682192)