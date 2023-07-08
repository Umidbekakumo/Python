height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

num_height = float(height)
num_weight = int(weight)

bam = num_weight / (num_height * num_height)
bam_int = int(bam)
print(bam_int)
