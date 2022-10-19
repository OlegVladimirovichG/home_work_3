import random
rnd_lst = [random.randint(0, 10) for _ in range(6)]
new_lst = []
mult = 1
for i in range((len(rnd_lst) + 1) // 2):
    mult = rnd_lst[i] * rnd_lst[-i-1]
    new_lst.append(mult)
print(rnd_lst)
print(new_lst)