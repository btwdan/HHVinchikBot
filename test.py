import random

print(ord('a'))

random_chr = random.randint(ord('a'), ord('z'))
rnd_word = random.choice(chr(random_chr))

print(rnd_word)