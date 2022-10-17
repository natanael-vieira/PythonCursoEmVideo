num = [2, 4, 8, 9]
print(num)

num[3] = 7
print(num)

num.append(1)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos.')

num.insert(2, 0)
print(num)

num.pop()
print(num)

num.pop(2)
print(num)

num.insert(2, 2)
print(num)

num.remove(2)
print(num)

if 3 in num:
    num.remove(3)
else:
    print('Não achei o número 3.')

print(num)
