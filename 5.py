n = int(input('Сколько рыбов у первого? '))
k = int(input('Сколько рыбов у второго? '))
if n < k:
    print('Первый неудачник, у него', n, 'рыбов')
elif k < n:
    print('Второй неудачник, у него', k, 'рыбов')
else:
    print('Ничья')