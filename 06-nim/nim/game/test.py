import random 

num_pile = random.randint(2, 5)
print(num_pile)

pile_number = []
for i in range(num_pile):
    i += 1
    pile_number.append(i)

print(pile_number)


for i in range(1): 
    print("-" * 20)
    for s in range(num_pile):
        stones = random.randint(1, 9)
        num_stones = "O" * stones
        print(f"{pile_number[s]}: {num_stones}")
    print("-" * 20)

