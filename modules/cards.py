import random


suits = ( "hearts", "diamonds", "clubs", "spades")
cards = []
values = range(1, 18)
# print(list(values))

for s in suits:
    for v in values:
        cards.append("{0} of {1}".format(v, s))
print(cards)

# print(random.choice(cards))

random.shuffle(cards)
print(" Shuffled cards ---> {}".format(cards))