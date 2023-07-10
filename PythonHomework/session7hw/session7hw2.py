# TASK 3 AND 4

animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey', 'crocodile', 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 'kangaroo', 'monkey']
word_count = {}


for animal in animal_list:
    if animal in word_count:
        word_count[animal] += 1
    else:
        word_count[animal] = 1


print(word_count)



List:
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

    counter = 
    time_sum = 
    ## Pseudo code for Task 4 
# for loop list:
    #if statement that will find the connections to rome:
        # counter + 1 
        sum += time value connections[1][2]
#you need to use .format or f{} ----> fstring 
print(' {counter} connections lead to Rome with an average flight time of {time_sum/counter} minutes
 ')




{} connections lead to Rome with an average flight time of {} minutes


