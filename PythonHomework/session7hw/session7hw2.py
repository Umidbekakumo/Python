# TASK 3 AND 4

animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey', 'crocodile', 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 'kangaroo', 'monkey']
word_count = {}


for animal in animal_list:
    if animal in word_count:
        word_count[animal] += 1
    else:
        word_count[animal] = 1


print(word_count)



