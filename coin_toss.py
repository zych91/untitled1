from random import randint
number = int(input("Ile razy chcesz rzucić?"))
heads = 0
tails = 0

for i in range(number):
    flip = int(randint(0, 1))
    if flip == 0:
        print("Heads!")
        heads += 1
    else:
        print("Tails!")
        tails += 1

print(f"Wypadło {heads} headsów i {tails} tailsów.")
