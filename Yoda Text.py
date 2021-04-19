import random

random.seed(43)
# your sentence is assigned to the variable
sentence = input().split()
random.shuffle(sentence)
# write your python code below


# shows the message
print(' '.join(sentence))