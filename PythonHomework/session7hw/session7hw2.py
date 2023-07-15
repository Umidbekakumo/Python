# TASK 3 AND 4

# animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey', 'crocodile', 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 'kangaroo', 'monkey']
# word_count = {}


for animal in animal_list:
       word_count[animal] += 1
        else:
         word_count[animal] = 1
    # ## Pseudo code for Task 4 
#for loop list:
    #if statement that will find the connections to rome:
        # counter + 1 
        #you need to use .format or f{} ----> fstring 

#  print(word_count)



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

counter = 0 
time_sum = 0 

for connection in connections:
    city_from, city_to, flight_time = connection 
    if city_to == 'Rome':
        counter += 1
        time_sum += flight_time 
print(f' {counter} connections lead to Rome with an average flight time of {time_sum/counter} minutes')


